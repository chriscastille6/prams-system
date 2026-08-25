import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import assert from "node:assert/strict";

const here = dirname(fileURLToPath(import.meta.url));
const require = createRequire(import.meta.url);
const {
  DEFAULT_CITI_FOLDER,
  parseAllowedCitiFolderUrl,
  safeCitiFolderUrl,
} = require("./citi_folder_url.js");

const GOOD = DEFAULT_CITI_FOLDER;
const GOOD_SHARED = GOOD + "?usp=sharing";
const GOOD_MULTI =
  "https://drive.google.com/drive/u/0/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi";
const SCRIPT_URL = ["java", "script:"].join("") + "alert(1)";
const DATA_URL = ["data:", "text/html,", "phishing"].join("");
const AUTH_URL =
  "https://" +
  ["reviewer", "token"].join(":") +
  "@drive.google.com/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi";

test("accepts Nicholls Drive folder URLs", () => {
  assert.equal(parseAllowedCitiFolderUrl(GOOD), GOOD);
  assert.equal(parseAllowedCitiFolderUrl("  " + GOOD + "  "), GOOD);
  assert.equal(
    parseAllowedCitiFolderUrl(GOOD.replace("drive.google.com", "DRIVE.GOOGLE.COM")),
    GOOD
  );
  assert.equal(parseAllowedCitiFolderUrl(GOOD_SHARED), GOOD_SHARED);
  assert.equal(parseAllowedCitiFolderUrl(GOOD_MULTI), GOOD_MULTI);
  assert.equal(safeCitiFolderUrl(GOOD), GOOD);
});

test("rejects script and non-https schemes", () => {
  for (const raw of [
    SCRIPT_URL,
    SCRIPT_URL.toUpperCase(),
    "  " + SCRIPT_URL,
    DATA_URL,
    "http://drive.google.com/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
    "//drive.google.com/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
    "/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
  ]) {
    assert.equal(parseAllowedCitiFolderUrl(raw), null, raw);
    assert.equal(safeCitiFolderUrl(raw), GOOD, raw);
  }
});

test("rejects other hosts and embedded credentials", () => {
  for (const raw of [
    "https://evil.example/phish",
    "https://drive.google.com.evil.example/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
    "https://evil.example/drive.google.com/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
    "https://docs.google.com/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
    AUTH_URL,
    "https://drive.google.com:8443/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
  ]) {
    assert.equal(parseAllowedCitiFolderUrl(raw), null, raw);
    assert.equal(safeCitiFolderUrl(raw), GOOD, raw);
  }
});

test("rejects Drive URLs that are not folder links", () => {
  for (const raw of [
    "https://drive.google.com/",
    "https://drive.google.com/file/d/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi/view",
    "https://drive.google.com/open?id=1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi",
    "https://drive.google.com/drive/folders/../file/d/x",
  ]) {
    assert.equal(parseAllowedCitiFolderUrl(raw), null, raw);
  }
});

test("empty or missing values fall back to the default folder", () => {
  assert.equal(safeCitiFolderUrl(""), GOOD);
  assert.equal(safeCitiFolderUrl(null), GOOD);
  assert.equal(safeCitiFolderUrl(undefined), GOOD);
  assert.equal(parseAllowedCitiFolderUrl(""), null);
});

test("registry.html never assigns imported citi_folder_url to href directly", () => {
  const html = readFileSync(join(here, "registry.html"), "utf8");
  assert.match(html, /citi_folder_url\.js/);
  assert.match(html, /safeCitiFolderUrl|parseAllowedCitiFolderUrl/);
  assert.doesNotMatch(
    html,
    /openCitiFolder\.href\s*=\s*registry\.citi_folder_url/
  );
  assert.doesNotMatch(
    html,
    /openCitiFolder\.href\s*=\s*data\.citi_folder_url/
  );
});
