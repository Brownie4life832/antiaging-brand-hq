// Shared-code gate for the research explorer (Cloudflare Pages advanced mode).
// Anyone with the code can view: at the browser prompt, put the code in the PASSWORD
// field (any username). Change the code: edit ACCESS_CODE and redeploy.
// Remove the gate entirely: delete this file and redeploy.
const ACCESS_CODE = "longevity2026";

export default {
  async fetch(request, env) {
    const header = request.headers.get("Authorization") || "";
    if (header.startsWith("Basic ")) {
      try {
        const decoded = atob(header.slice(6));
        const pass = decoded.slice(decoded.indexOf(":") + 1);
        if (pass === ACCESS_CODE) return env.ASSETS.fetch(request);
      } catch (e) { /* fall through to prompt */ }
    }
    return new Response("This research site is private. Enter the access code as the password (any username).", {
      status: 401,
      headers: { "WWW-Authenticate": 'Basic realm="Research Explorer — enter the access code as the password"' },
    });
  },
};
