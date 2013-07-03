player

Endpoint Player;
Endpoint PlayerHelper;

Sequences {
 GameInSession: Player.doNothing -> PlayerHelper.checkServer;
 AddUser: Player.addName -> PlayerHelper.sendServer;
 SendAnswer: Player.send -> PlayerHelper.checkAnswer; 
 DisplayMessage: PlayerHelper.doNothing -> Player.printMessage;
 GetAnagram: Player.doNothing -> PlayerHelper.setAnagram;
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
Sequence GameInSession() returns TrueFalse game_status{
  Player.doNothing {
  }
  PlayerHelper.checkServer {
    game_status = game_server.get_game_status();
  }
}

Sequence AddUser() {
  Player.doNothing {
    //List (element: Text) test_list = 
  
  }
  PlayerHelper.sendServer {
    Text message = username + " has entered the game room.";
    game_server.broadcastMessage(message);
    game_server.add_user(username, self);
  }
}

Sequence SendAnswer(Text answer) returns TrueFalse valid_answer{
  Player.doNothing{}
  PlayerHelper.checkAnswer {
    valid_answer = game_server.check_word(answer, username);
  }
}

Sequence DisplayMessage(Text message) {
  PlayerHelper.doNothing{}
  Player.printMessage {
    print_message(message);
  }
}

Player {
  List (element: Text) usedWords;
  Function (in: Text; returns: Nothing) print_message;
  onCreate(Text name, Function (in: Text; returns: Nothing) prntmsg) {
    username = name;
    print_message = prntmsg;
  }

  Public Function get_anagram() returns Text{
    return GetAnagram();
  }

  Public Function game_in_session() returns TrueFalse {
    return GameInSession();
  }

  Public Function send_answer(Text answer) {
    if (answer in usedWords) {
      print_message("Word already used.");
    } else if (SendAnswer(answer)) {
      usedWords.append(answer);
    } else {
      print_message(answer + " is not a valid word.");
    }
  }

  Public Function add_to_server() {
    AddUser();
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
