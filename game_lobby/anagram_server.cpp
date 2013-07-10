anagram_server

Endpoint AnagramServer;

Struct player_data {
  Endpoint player_helper;
  Number score;
}

AnagramServer {
  Map(from: Text, to: Endpoint) waiting_room;
  Map(from: Text, to: Struct player_data) game;
  List (element: Text) solutions;
  Text anagram;
  TrueFalse game_in_session;
  onCreate() {
    game_in_session = False;
  }

  Public Function set_solution(Text init_anagram, List (element: Text) solution){
    anagram = init_anagram;
    solutions = solution;
  }
  Public Function start_game() {
    for (Text username in game) {
          game[username].score = 0;
	  game[username].player_helper.get_new_message("Game has started.");
    }
    game_in_session = True;
  }
  
  Public Function get_game_status() returns TrueFalse {
    return game_in_session;
  }
 
  Public Function return_anagram() returns Text{
    return anagram;
  }

  Public Function return_solutions() returns List(element: Text) {
    return solutions;
  }

  Public Function get_player_count() returns Number {
    return len(game);
  }

  Public Function get_scores() returns Map(from: Text, to: List(element: Text)) {
    return game;
  }

  Public Function add_score(Text username, Number points) returns Number{
    game[username].score += points;
    return game[username].score;
  }

  Public Function add_player(Text username, Endpoint pt) {
    Text message = username + " is in the game room.";
    Struct player_data player;
    player.score = 0;
    player.player_helper = pt;
    game[username] = player;
    broadcastWaitingMessage(message);
  }

  Public Function add_to_waiting(Text username, Endpoint pt) {
    Text message = username + " has entered the waiting room.";
    broadcastWaitingMessage(message);
    waiting_room[username] = pt;
  }

  Public Function remove_from_waiting(Text username) {
    Text message = username + " has left the waiting room.";
    waiting_room.remove(username);
    broadcastWaitingMessage(message);
  }

  Public Function get_score(Text username) returns Number {
    return game[username].score;
  }

  Public Function remove_user(Text username) {
    game.remove(username);
  }

  Public Function broadcastMessage(Text message) {
    for (Text username in game) {
      game[username].player_helper.get_new_message(message);
    }
  }

  Public Function broadcastWaitingMessage(Text message) {
    for (Text username in waiting_room) {
      waiting_room[username].get_new_message(message);
    }
  }

  Public Function end_game() {
    game_in_session = False;
    broadcastMessage("Game Over.");
    for (Text username in game) {
      Text score = username + ' - ' + toText(game[username].score);
      broadcastMessage(score);
    }
    broadcastMessage("Press ENTER to continue.");
    game = {};
  }
}
