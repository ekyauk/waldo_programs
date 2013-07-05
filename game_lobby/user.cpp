userfile

Endpoint User;
Endpoint UserHelper;

Sequences {
 AddUser: User.doNothing -> UserHelper.sendServer;
 SendMessage: User.send -> UserHelper.updateUsers; 
 DisplayMessage: UserHelper.doNothing -> User.printMessage;
 Quit: User.doNothing -> UserHelper.notify;
 SendPrivate: User.doNothing -> UserHelper.sendMessage -> User.checkSent;
 PrintUsers: User.doNothing -> UserHelper.get_list -> User.print_list;
}

Peered 
{
  Text username;
}

Sequence Quit(TrueFalse inGame) {
  User.doNothing {}
  UserHelper.notify {
    Text message;
    if (inGame) {
      message = " is playing a game.";
    } else {
      message = " has left the chatroom.";
    }
    message = username + message;
    chat_server.broadcastMessage(message);
    chat_server.remove_user(username);
  }
}

Sequence AddUser(TrueFalse inGame) {
  User.doNothing {}
  UserHelper.sendServer {
    Text message;
    if (inGame) {
      message = " is back from a game.";
    } else {
      message = " has entered the chatroom.";
    }
    message = username + message;
    chat_server.broadcastMessage(message);
    chat_server.add_user(username, self);
  }
}

Sequence SendPrivate(Text receiver, Text message) {
  TrueFalse message_sent;
  User.doNothing{}
  UserHelper.sendMessage {
    message = 'private message from ' + username + ': ' + message;
    message_sent = chat_server.send_message(receiver, message);
  }
  User.checkSent {
    if (not message_sent) {
      message = receiver + ' does not exist in chat.';
      print_message(message);
    }
  }
}

Sequence SendMessage(Text message) {
  User.send {
  }
  UserHelper.updateUsers{
    chat_server.broadcastMessage(message);
  }
}

Sequence DisplayMessage(Text message) {
  UserHelper.doNothing{}
  User.printMessage {
    print_message(message);
  }
}

Sequence PrintUsers() {
  List(element: Text) users_list;

  User.doNothing{}

  UserHelper.get_list {
    users_list = chat_server.get_users();
  }

  User.print_list {
    print_message('Users in chat:');
    print_message('');
    for (Text user in users_list) {
      print_message(user);
    }
    print_message('');
  }

}

User {
  Function (in: Text; returns: Nothing) print_message;
  onCreate(Text name, Function (in: Text; returns: Nothing) prntmsg) {
    username = name;
    print_message = prntmsg;
  }
  Public Function send_message(Text message) {
    SendMessage(message);
  }
  Public Function add_to_server(TrueFalse inGame) {
    AddUser(inGame);
  }

  Public Function quit(TrueFalse inGame) {
    Quit(inGame);
  }

  Public Function private_message(Text receiver, Text message) {
    SendPrivate(receiver, message);
  }
  
  Public Function print_users() {
    PrintUsers();
  }

}


UserHelper {
  Endpoint chat_server;
  onCreate(Endpoint server) {
    chat_server = server;
  }
  Public Function get_new_message(Text message) returns Nothing {
    DisplayMessage(message);
  }
}
