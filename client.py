class MarchingCubes2D:
    """
    Marching Squares / 2D Isosurface Extractor.
    Extracts isocontour line segments crossing 2D grid cells.
    """
    def extract_isolines(self, grid, isovalue):
        nx = len(grid)
        ny = len(grid[0])
        segments = []
        for x in range(nx - 1):
            for y in range(ny - 1):
                corners = [grid[x][y], grid[x+1][y], grid[x+1][y+1], grid[x][y+1]]
                case = sum((1 << i) for i, c in enumerate(corners) if c >= isovalue)
                if case not in (0, 15):
                    segments.append(((x + 0.5, y), (x + 0.5, y + 1)))
        return segments
