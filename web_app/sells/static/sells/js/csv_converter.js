class csvExport {
    constructor(table, header = true) {
        this.table = table;
        this.rows = Array.from(table.querySelectorAll("tr"))
    }
    exportCsv() {
        const lines = [];
        const ncols = this.long_row();

        for (const row of this.rows) {
            let line = '';
            for (let i=0; i < ncols; i++) {

                if (row.children[i] !==undefined) {
                    line += row.children[i].textContent;
                }
                line += i !== ncols - 1 ? ";" : "";
            }
            lines.push(line)

        }
        for (let j=1; j < ncols; j++) {
            lines[j] = String(lines[j]).replace(/\n/gi, '');

        }
        return lines.join('\n');

    }

    long_row() {
        return this.rows.reduce((length, row) => (row.childElementCount > length ? row.childElementCount : length), 0)
    }
}

const btnExport = document.querySelector('#btnExport')
const tableElement = document.querySelector('table')

btnExport.addEventListener("click", () => {
    const obj = new csvExport(tableElement)
    const csv_data = (obj.exportCsv());
    const blob = new Blob([csv_data], {type: "text/csv" });

    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download='sales.csv';
    a.click();

    setTimeout(() => {
        URL.revokeObjectURL(url);
    }, 500);
    });