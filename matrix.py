class Matrix:
    def __init__(self, data) -> None:
        if not self.is_valid_matrix(data) and len(data) < 0:
            raise ValueError("Invalid input, the data entered is not a valid matrix")
        self.data = data
        self.rows = len(data[0])
        self.cols = len(data[0]) if self.rows > 0 else 0

   
    def is_valid_matrix(self, data) -> bool:
        # checks if the matrix is a valid matrix
        if not isinstance(data, list) and len(data) < 0:
            return False
        
        rows_length = len(data[0])
        return all(isinstance(row, list) and len(row) == rows_length for row in data)
  
   
    def __repr__(self) -> str:
        # returns a string representation of the matrix
        return "\n".join(["\t".join(map(str, row)) for row in self.data])
    
    
    def get_items(self, row, col) -> int:
        # returns the element in the matrix at a particular row and column position
        size_of_matrix = len(self.data[0])
        if 0 <= row > size_of_matrix and 0 <= col > size_of_matrix:
            raise IndexError("the row or col number is bigger that the matrix size")
        else:
            return self.data[row][col]
        
    
    def set_items(self, row, col) -> None:
        # users can change the placement of a matrix
        size_of_matrix = len(self.data[0])
        if 0 <= row > size_of_matrix and 0 <= col > size_of_matrix:
            raise IndexError("the row or col number is bigger that the matrix size")
        else:
            self.data[row][col]
            print(f"data at location row{row} : col{col} has been updated")


    def get_row(self, row) -> list:
        # returns the specific row
        if 0 <= row < self.rows:
            return self.data[row]
        else:
            raise IndexError("beyond the index of the matrix")
    
    
    def get_column(self, col) -> list:
        # returns the specific column
        if 0 <= col < self.cols:
            return [ self.data[row][col] for row in range(self.rows)]
        else:
            raise IndexError("beyond the index of the matrix")

    