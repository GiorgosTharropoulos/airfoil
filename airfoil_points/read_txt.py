class TxtReader:
    def __init__(self, file):
        self.file = file

    def read_x_y(self):
        """Get two list of floats from a .txt file. Split each line of text
        and convert each array to an array of floats.

        #Reference
        https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats

        Returns:
            [float array]: [Array of floats for x coordinate]
            [float array]: [Array of floats for y coordinate]
        """
        chi = []
        psi = []
        with open(self.file, "r") as f:
            for line in f:
                [x, y] = line.split()
                chi.append(x)
                psi.append(y)
        x = [float(i) for i in chi]
        y = [float(i) for i in psi]
        return x, y


if __name__ == "__main__":
    reader = TxtReader("naca0012.txt")
    x, y = reader.read_x_y()
    print(x)
    print(y)
