class PascalTriangle:
    def perform(self, numRows):
        if numRows == 0:
            return []

        triangle = [[1]];

        for i in range(0, numRows-1):
            previous_row = triangle[-1]
            current_row = [1]
            for j in range(0, i):
                current_row.append(previous_row[j] + previous_row[j+1])

            current_row.append(1)
            triangle.append(current_row)

        return triangle

