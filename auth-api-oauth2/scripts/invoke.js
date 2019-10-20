const u = require("./utils");
const exec = require("child_process").execSync;

// TODO: This is waiting on https://github.com/serverless/serverless/issues/4746
console.log("This is waiting on https://github.com/serverless/serverless/issues/4746");
process.exit(1);

if (process.argv.length < 3) {
  exec("yarn build");
  const files = u.getFiles("./bin");
  if (files.length !== 1) {
    console.error("You must specify a function name since you have multiple functions. ");
    process.exit(1);
  } else {
    console.log(`sls invoke ./${files[0]}`);
    exec(`sls invoke local -f ${files[0]}`);
    process.exit(0);
  }
} else if (process.argv.length === 3) {
  const fn = process.argv[2];
  console.error("Script does not work...");
}
