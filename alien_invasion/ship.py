import	pygame

class Ship():
	def  __init__(self,ai_settings,screen):
		self.screen=screen
		self.ai_settings=ai_settings

		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()

		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		self.center=float(self.rect.centerx)

		self.moveing_right=False
		self.moveing_left=False
	def blitme(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		if self.moveing_right:
			self.center+=float(self.ai_settings.ship_speed_factor)
		elif self.moveing_left:
			self.center-=float(self.ai_settings.ship_speed_factor)
		#设置边界检查
		if self.center<0:
			self.center=0
		elif self.center>self.screen_rect.right:
			self.center=self.screen_rect.right
		self.rect.centerx=self.center