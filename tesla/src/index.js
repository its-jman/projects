const tsla = require("teslajs");

(async () => {
  const { response, body, authToken, refreshToken } = await tsla.loginAsync(
    "drm.mhk.ks@gmail.com",
    "64Yrsold"
  );

  console.log("RESP");
  console.log(response);
  console.log(body);
  console.log(authToken);
  console.log(refreshToken);
})();
