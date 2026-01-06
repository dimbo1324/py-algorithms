class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        vis_coords = {(x, y)}

        for step in path:
            print(step)
            match step:
                case "N":
                    dx, dy = 0, 1
                case "S":
                    dx, dy = 0, -1
                case "E":
                    dx, dy = 1, 0
                case "W":
                    dx, dy = -1, 0
                case _:
                    return False

            x += dx
            y += dy
            cur_coords = (x, y)

            if cur_coords in vis_coords:
                return True
            vis_coords.add(cur_coords)

        return False


path = "NESWW"
print(Solution().isPathCrossing(path))
