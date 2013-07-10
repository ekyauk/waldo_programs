player

Endpoint Player;
Endpoint PlayerHelper;

Sequences {
 GameInSession: Player.doNothing -> PlayerHelper.checkServer;
 AddUser: Player.doNothing -> PlayerHelper.sendServer;
 AddPoints: Player.doNothing -> PlayerHelper.addPoints -> Player.displayMessage;
 DisplayMessage: PlayerHelper.doNothing -> Player.printMessage;
 GetAnagram: Player.doNothing -> PlayerHelper.setAnagram;
 GetSolutions: Player.doNothing -> PlayerHelper.setList;
 JoinWaiting: Player.doNothing -> PlayerHelper.addPlayer;
 LeaveWaiting: Player.doNothing -> PlayerHelper.removePlayer;
 SendToWaiting: Player.doNothing -> PlayerHelper.sendMessage;
}

Peered 
{
  Text username;
}

Sequence GetAnagram() returns Text anagram {
  Player.doNothing{}
  PlayerHelper.setAnagram {
    anagram = game_server.return_anagram();
  }
}

Sequence GetSolutions() returns List (element: Text) solutions{
  Player.doNothing{}
  PlayerHelper.setList {
    solutions = game_server.return_solutions();
  }
}
Sequence GameInSession() returns TrueFalse game_status{
  Player.doNothing {
  }
  PlayerHelper.checkServer {
    game_status = game_server.get_game_status();
  }
}

Sequence AddUser() {
  Player.doNothing {  
  }
  PlayerHelper.sendServer {
    game_server.add_player(username, self);
  }
}

Sequence JoinWaiting() {
  Player.doNothing {}
  PlayerHelper.addPlayer {
     game_server.add_to_waiting(username, self);
  }
}

Sequence LeaveWaiting() {
  Player.doNothing{}
  PlayerHelper.removePlayer {
    game_server.remove_from_waiting(username);
  }
}

Sequence AddPoints(Number points) {
  Text message;
  Player.doNothing{}
  PlayerHelper.addPoints {
    Number score = game_server.add_score(username, points);
    message = 'Score: ' + toText(score);
  }
  Player.displayMessage {
    print_message(message);
  }
}

Sequence DisplayMessage(Text message) {
  PlayerHelper.doNothing{}
  Player.printMessage {
    print_message(message);
  }
}

Sequence SendToWaiting(Text message) {
  Player.doNothing{}
  PlayerHelper.sendMessage{
    game_server.broadcastWaitingMessage(message);
  }
}

Player {
  Function (in: Text; returns: Nothing) print_message;
  onCreate(Text name, Function (in: Text; returns: Nothing) prntmsg) {
    username = name;
    print_message = prntmsg;
  }

  Public Function get_anagram() returns Text{
    return GetAnagram();
  }

  Public Function get_solutions() returns List(element: Text){
    return GetSolutions();
  }

  Public Function game_in_session() returns TrueFalse {
    return GameInSession();
  }

  Public Function add_points(Number points) {
    AddPoints(points);
  }

  Public Function add_to_game() {
    AddUser();
  }
  Public Function join_waiting_room() {
    JoinWaiting();
  }

  Public Function leave_waiting() {
    LeaveWaiting();
  }
  Public Function send_to_waiting(Text message) {
    message = "from " + username + " in the waiting room: " + message;
    SendToWaiting(message);
  }
}


PlayerHelper {
  Endpoint game_server;
  onCreate(Endpoint server) {
    game_server = server;
  }
  Public Function get_new_message(Text message) returns Nothing {
    DisplayMessage(message);
  }
}
