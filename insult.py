import random

def isprime(n):
	if n == 2:
		return 1
	if n % 2 == 0:
		return 0
	max = n**0.5+1
	i = 3
	while i <= max:
		if n % i == 0:
			return 0
		i+=2
	return 1

def asl():
	a = random.randint(1,9001)
	if isprime(a):a=12;
	s = {
		1:'m',
		2:'f',
		3:'robot',
		4:'raptor',
		5:'demigod',
		6:'neckbeard',
		7:'plant',
		8:'shoe',
		9:'flounder',
		10:'dolphin',
		11:'omni',
		12:'anti-spiral',
		13:'hokage',
		14:'ninja',
		15:'cyborg',
		16:'pirate',
		17:'slut',
		18:'dog',
		19:'cat',
		20:'squid',
		21:'kid',
		22:'your favorite anime character',
		23:'ur waifu',
		24:'slime',
		25:'doge',
		26:'living meme',
		27:'stand',
		28:'undead',
		29:'burn victom',
		30:'b8',
		31:'gr8 b8',
		32:'yokai',
		33:'shrine maiden',
		34:'loli',
		35:'2hu',
		36:'edge lord',
		
	}
	l = {
		1:'cali',
		2:'space',
		3:'dark side of the moon',
		4:'bottom of the ocean',
		5:'ur moms box',
		6:'behind you',
		7:'bathroom',
		8:'ur gf',
		9:'fuck you',
		10:'a coffin',
		11:'in bed',
		12:'in traffic',
		13:'girls only bus',
		14:'your favorite anime',
		15:'your least favorite anime',
		16:'ur ex',
		17:'gensokyo',
		18:'a well',
	}
	return str(a)+'/'+s.get(random.randint(1,len(s)))+'/'+l.get(random.randint(1,len(l)))

		

def comeback():
	y = {
		1:'you dirty gook',
		2:'because you touch yourself at night',
		3:'maybe if you weren\'t such a fgt',
		4:'ur mom',
		5:'cause I\'m not a little bitch',
		6:'cause you\'re a little bitch',
		7:'ur just mad cuz\' I\'m stylin\' on u',
		8:'maybe you\'d know if you\'d stop bouncing on yo daddy\'s dick and read a book',
		9:'ur waifu is trash',
		10:'we\'re all dumber for hearing that',
		11:'ask ur mom',
		12:'you\'re why your father left',
		13:'jet fuel can\'t melt steel beams but your fat ass can bend them',
		14:': 7/11 was an inside job but you were an accident',
		15:'you\'re tacky and I hate you',
		
		
	}
	return y.get(random.randint(1,len(y)), 'Ur mom')
