DROP TABLE IF EXISTS recommendations;

CREATE TABLE recommendations (
    url text,
    group_label text,
    label text,
    tags text[],
    kind text
);

CREATE UNIQUE INDEX recommendations_url_idx ON recommendations(url text_ops);
CREATE INDEX recommendations_kind_idx ON recommendations(kind text_ops);
