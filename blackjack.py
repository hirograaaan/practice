import random

#デッキを初期化する
def init_deck():
  numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  suits = ['H', 'S', 'D', 'C']
  deck = [(suit, number) for suit in suits for number in numbers]
  random.shuffle(deck)
  return deck

#カードの合計ポイントを計算
def calc(cards):
  score = 0
  for (suit, number) in cards:
    if number == 'A':
      score += 11
    elif number in ['J', 'Q', 'K']:
      score += 10
    else:
      score += int(number)
    
  # A の処理
  for (suit,number) in cards:
    if number == 'A' and score > 21:
      score -= 10
  
  return score

#勝者を判定する
def winner(player_score, dealer_score):
  if player_score == dealer_score:
    return "引き分け"
  elif dealer_score > 21:
    return "プレイヤーの勝ち！"
  elif player_score > 21:
    return "プレイヤーの負け！"
  elif player_score > dealer_score:
    return "プレイヤーの勝ち！"
  else:
    return "プレイヤーの負け！"
  
#ブラックジャックのメイン部分
def blackjack():
  player_money = 50 #持ち金

  while player_money > 0:
    print("現在の持ち金: ${}".format(player_money))
    bet = int(input("賭け金を入力してください: "))
    if bet > player_money:
      print("持ち金よりも大きい賭け金はできません。")
      continue

    deck = init_deck()
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]
    game_over = False

    while not game_over:
      player_score = calc(player_cards)
      dealer_score = calc(dealer_cards)

      print("あなたのカードは{}、合計ポイントは{}です。".format(player_cards, player_score))

      if player_score > 21:
        game_over = True
      else:
        game_continue = input("カードを引く場合は'y'を、終了する場合は'n'を入力してください。")
        if game_continue == 'y':
          player_cards.append(deck.pop())
        elif game_continue == 'n':
          game_over = True
        else:
          print("無効な入力です。'y'または'n'を入力してください。")
    
    while dealer_score != 0 and dealer_score < 17:
      dealer_cards.append(deck.pop())
      dealer_score = calc(dealer_cards)

    print("あなたの最終的なカードは{}、合計ポイントは{}です。".format(player_cards, player_score))
    print("ディーラーの最終的なカードは{}、合計ポイントは{}でした。".format(dealer_cards, dealer_score))
    result = winner(player_score, dealer_score)
    print(result)

    if result == "プレイヤーの勝ち！":
      player_money += bet
    elif result == "プレイヤーの負け！":
      player_money -= bet
  
    play_again = input("もう一度プレイしますか？ 続ける場合は'y'を入力してください: ")
    if play_again != 'y':
      break

  print("ゲーム終了。お疲れ様でした！")

#ゲームを開始する  
blackjack()