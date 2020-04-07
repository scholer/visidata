#!/usr/bin/env python3

import sys
import vdtui


class TsvSheet(vdtui.Sheet):
    rowtype = 'rows'
    columns = [vdtui.ColumnItem('tsv', 0)]

    @vdtui.asyncthread
    def reload(self):
        self.rows = []

        with open(self.source, encoding=vdtui.options.encoding) as fp:
            for line in fp:
                line = line[:-1]
                if line:
                    self.addRow(line.split('\t'))

        self.columns = [vdtui.ColumnItem(colname, i) for i, colname in enumerate(self.rows[0])]
        self.rows = self.rows[1:]


def viewtsv_cli():
    vdtui.run(*(TsvSheet(fn, source=fn) for fn in sys.argv[1:]))


if __name__ == "__main__":
    viewtsv_cli()
