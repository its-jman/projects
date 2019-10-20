const tf = require("template-file");
const path = require("path");
const fs = require("fs");
const replace = require("replace");

if (process.argv.length !== 4) {
  console.error("Usage: \n\tyarn add-endpoint [endpoint-name] [http-method]");
  process.exit(1);
}

const data = {
  service: process.argv[2],
  method: process.argv[3].toUpperCase()
};
data.fullPath = `${data.service}-${data.method}`;

const serviceDir = path.join(__dirname, "..", "cmd", `${data.fullPath}`);
if (fs.existsSync(path.join(serviceDir, "main.go"))) {
  console.error(`Endpoint [${data.service}] already exists.`);
  process.exit(1);
} else {
  fs.mkdirSync(serviceDir);
}

const definitionRes = tf
  .renderTemplateFile(path.join(__dirname, "templates", "definition.yml.template"), data)
  .then((str) => {
    fs.writeFileSync(path.join(serviceDir, "definition.yml"), str);
  });

const mainRes = tf
  .renderTemplateFile(path.join(__dirname, "templates", "main.go.template"), data)
  .then((str) => {
    fs.writeFileSync(path.join(serviceDir, "main.go"), str);
  });

const serverlessPath = path.join(__dirname, "..", "serverless.yml");
const serverlessBackupPath = path.join(__dirname, "..", "serverless-backup.yml");
fs.copyFileSync(serverlessPath, serverlessBackupPath);

// Do NOT read yaml and output new yaml. No comments would be transferred.
replace({
  paths: [serverlessPath],
  regex: /functions:/,
  replacement: `$&\n  - \${file(./cmd/${data.fullPath}/definition.yml)}`
});
