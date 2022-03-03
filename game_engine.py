import sys,time,random
import pickle 

#TO DO: ACERTAR O NUMERO DO CAP AO SER FINALIZADO
#TO DO: POSSIBILITAR QUE O USUÁRIO ESCOLHA O CAPITULO A SER JOGADO

def slow_type(t):#Velocidade do texto
    typing_speed = 100 #wpm
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def get_input(valid_input: list):#Tratamento de erro caso usuário não selecione uma opção válida
  while True:
    user_entered = input()
    if user_entered not in valid_input:
      print("Input inválido. Por favor, use um \
              dos seguintes inputs:\n")
      print(valid_input)
      user_entered = None
    else:
      return user_entered


def display_page_text(lines: list):
  for line in lines:
    slow_type(line)
    # Usuário deve pressionar enter para continuar
    get_input([""])


def get_response(options: list): #Pega a resposta do usuário dentre as opções
  for index, option in enumerate(options):
    print(str(index) + ". " + option[0])
  
  valid_inputs = [str(num) for num in range(len(options))]

  option_index = int(get_input(valid_inputs))

  return options[option_index][1]

def next_chap(cap):
  continue_game = False
  print("Fim do capítulo {}, deseja continuar?(S/N)".format(cap))
  while True:
      valid_answer = ("S","N")
      answer_continue = input("")
      answer_continue = answer_continue.upper()
      if answer_continue not in valid_answer:
          print("Input inválido. Por favor, use um dos seguintes inputs:\n")
          print(str(valid_answer[0]) + '\n' + str(valid_answer[1]))
          answer_continue = None
      
      if answer_continue == "N":
          print('Fim de jogo')
          return continue_game

      if answer_continue == "S":
          print('Prox cap')
          continue_game = True
          chapter_two()
          return continue_game



def story_flow(story: dict):
  curr_page = 1
  cap = 0

  while curr_page != None:
    page = story.get(curr_page, None)
    
    if page == None:
      curr_page = None
      break

    display_page_text(page['Text'])
    
    if len(page['Options']) == 0:
      curr_page = None
      cap += 1
      if next_chap(cap) == False:
        break

    curr_page = get_response(page['Options'])
   
def chapter_two():
  story = {}
  with open('chapter2.bin', 'rb') as chapter2:
    story = pickle.load(chapter2)

  story_flow(story)

if __name__=='__main__':
    story = {}
    with open('chapter1.bin', 'rb') as chapter:
 
        story = pickle.load(chapter)

    story_flow(story)
