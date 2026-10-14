import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const inputPath = new URL("../Top-500-Brand-Names.xlsx", import.meta.url).pathname.replace(/^\/(.:\/)/, "$1");
const input = await FileBlob.load(inputPath);
const workbook = await SpreadsheetFile.importXlsx(input);
const result = await workbook.inspect({
  kind: "workbook,sheet,table,region",
  maxChars: 12000,
  tableMaxRows: 8,
  tableMaxCols: 14,
  tableMaxCellChars: 120,
});
console.log(result.ndjson);
