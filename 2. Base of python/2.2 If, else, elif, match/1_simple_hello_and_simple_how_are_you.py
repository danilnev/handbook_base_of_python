name, vibe = [input() for i in range(2)]
print('Как Вас зовут?',
      f'Здравствуйте, {name}!',
      'Как дела?',
      sep='\n')
match vibe:
    case 'хорошо':
        print('Я за вас рада!')
    case 'плохо':
        print('Всё наладится!')
