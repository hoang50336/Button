class Button():
    def __init__(self, pos, inputText, font):
        self.x = pos[0]
        self.y = pos[1]
        self.inputText = inputText
        self.font = font
        self.text = self.font.render(self.inputText, True, 'White')
        self.rect = self.text.get_rect(topleft=(self.x, self.y))

    def update(self, screen):
        screen.blit(self.text, (self.x+5, self.y))

    def Click(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.inputText, True, 'Green')
        else:
            self.text = self.font.render(self.inputText, True, 'White')