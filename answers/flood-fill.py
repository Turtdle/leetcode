def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc] == color:
        return image
    def fill(image, sr, sc, color, new_color):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != color:
            return
        image[sr][sc] = new_color
        fill(image, sr + 1, sc, color, new_color)
        fill(image, sr - 1, sc, color, new_color)
        fill(image, sr, sc + 1, color, new_color)
        fill(image, sr, sc - 1, color, new_color)
    fill(image, sr, sc, image[sr][sc], color)
    return image