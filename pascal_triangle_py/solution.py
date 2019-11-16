class PascalTriangle:

    def perform(self, numRows):

        triangle = [[1]];

        for i in range(0, numRows-1):

            previous_row = triangle[-1]
            current_row = []
            current_row.append(1)
            for j in range(0, i + 1 - 2 + 1):
                current_element = previous_row[j] + previous_row[j+1]
                current_row.append(current_element)

            current_row.append(1)

            triangle.append(current_row)

        return triangle

