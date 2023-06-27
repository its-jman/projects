import { $ } from "zx";
import fs from "fs";
import path from "path";
import open from "open";

let i = 0;

async function fetchPage(cursor) {
  i += 1;
  const key = `${cursor ?? "BASE"}.json`;
  const keyPath = path.join(".cache", key);

  if (fs.existsSync(keyPath)) {
    return JSON.parse(fs.readFileSync(keyPath));
  }

  const raw = await $`twitch api get /clips \
-q broadcaster_id=110176631 \
-q started_at=2022-06-18T23:48:34-07:00 \
-q ended_at=2022-06-22T23:48:34-07:00 ${
    cursor ? [`-q`, `after=${cursor}`] : ``
  }`;

  const all = JSON.parse(raw.stdout);

  fs.writeFileSync(keyPath, JSON.stringify(all));
  return all;
}

let cursor;
do {
  const { data, pagination } = await fetchPage(cursor);
  for (const clip of data) {
    await open(clip.url);
  }

  cursor = pagination.cursor;
} while (cursor);
