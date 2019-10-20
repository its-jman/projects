const u = require("./utils");
const parse = require("command-line-args");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const parserOptions = [
  { name: "packages", type: String, multiple: true, defaultOption: true },
  { name: "packageDir", alias: "d", type: String }
];
const parsed = parse(parserOptions);

const rootDir = parsed.packageDir || "cmd";
if (!(fs.existsSync(rootDir) && u.isDirectory(rootDir))) {
  console.error(`Package directory invalid: [${rootDir}]`);
  process.exit(1);
}

let packageDirs = [];
if (parsed.packages && parsed.packages.length > 0) {
  for (const p of parsed.packages) {
    const packageDir = path.join(rootDir, p);
    if (!u.isDirectory(packageDir)) {
      console.warn(`Package [${packageDir}] is not valid directory. `);
      continue;
    }
    packageDirs.push(packageDir);
  }
} else {
  packageDirs = u.getDirectories(rootDir);
  if (packageDirs.length === 0) {
    packageDirs = [rootDir];
  }
}

packageDirs = packageDirs.filter((packageDir) => {
  const packagePath = path.join(packageDir, "main.go");
  if (!fs.existsSync(packagePath)) {
    console.warn(`Package [${packageDir}] does not have a "main.go" file.`);
    return false;
  }
  return true;
});

if (packageDirs.length === 0) {
  console.error("No valid packages.");
  process.exit(1);
}

console.log("Building these packages:");
console.log(`\t${packageDirs.join("\n\t")}`);

for (const packageDir of packageDirs) {
  const packageName = packageDir.replace(`${rootDir}/`, "").replace("/main.go", "");

  execSync(`GOOS=linux go build -ldflags="-s -w" -o bin/${packageName} ./${packageDir}`);
  execSync(`chmod +x bin/${packageName}`);
}
