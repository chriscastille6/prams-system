/**
 * Allowlist for protocol-registry citi_folder_url values before they are
 * written to the "Open CITI folder" href. Imported JSON is untrusted.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api;
  }
  root.CobIrbCitiFolder = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  const DEFAULT_CITI_FOLDER =
    "https://drive.google.com/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi";

  const ALLOWED_HOST = "drive.google.com";
  const FOLDER_PATH = /^\/drive\/(?:u\/\d+\/)?folders\/[A-Za-z0-9_-]+\/?$/;

  function parseAllowedCitiFolderUrl(raw) {
    if (raw == null) return null;
    const trimmed = String(raw).trim();
    if (!trimmed) return null;
    let parsed;
    try {
      parsed = new URL(trimmed);
    } catch (_) {
      return null;
    }
    if (parsed.protocol !== "https:") return null;
    if (parsed.username || parsed.password) return null;
    if (parsed.port) return null;
    if (parsed.hostname.toLowerCase() !== ALLOWED_HOST) return null;
    if (!FOLDER_PATH.test(parsed.pathname)) return null;
    const path = parsed.pathname.replace(/\/+$/, "");
    return "https://" + ALLOWED_HOST + path + parsed.search;
  }

  function safeCitiFolderUrl(raw) {
    return parseAllowedCitiFolderUrl(raw) || DEFAULT_CITI_FOLDER;
  }

  return {
    DEFAULT_CITI_FOLDER,
    parseAllowedCitiFolderUrl,
    safeCitiFolderUrl,
  };
});
