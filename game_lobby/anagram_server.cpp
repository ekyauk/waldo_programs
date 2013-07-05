anagram_server

Endpoint AnagramServer;

AnagramServer {
  Map(from: Text, to: Endpoint) players;
  Map(from: Text, to: Number) player_scores;
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
    game_in_session = True;
    for (Text username in players) {
          player_scores[username] = 0;
	  players[username].get_new_message("Game has started.");
    }
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
    return len(players);
  }

  Public Function get_scores() returns Map(from: Text, to: List(element: Text)) {
    return player_scores;
  }

  Public Function add_score(Text username, Number points) returns Number{
    player_scores[username] += points;
    return player_scores[username];
  }

  Public Function add_user(Text username, Endpoint pt) {
    players[username] = pt;
  }

  Public Function get_score(Text username) returns Number {
    return player_scores[username];
  }

  Public Function remove_user(Text username) {
    players.remove(username);
    player_scores.remove(username);
  }

  Public Function broadcastMessage(Text message) {
    for (Text username in players) {
      players[username].get_new_message(message);
    }
  }

  Public Function end_game() {
    game_in_session = False;
    broadcastMessage("Game Over.");
    for (Text username in player_scores) {
      Text score = username + ' - ' + toText(player_scores[username]);
      broadcastMessage(score);
    }
    broadcastMessage("Press ENTER to continue.");
    players = {};
    player_scores = {};
  }
}
