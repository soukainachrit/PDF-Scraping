import Extract


def main(filename, page,case):
    Tables = []
    extractor=Extract.Extract(filename, page)
    if case == "1":
        Tables=extractor.extract_one_table_from_page()
        extractor.save_to_disk(Tables)
    if case == "2":
        Tables=extractor.extract_multiple_tables_from_page()
        extractor.save_to_disk(Tables)
