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
    Text msg;
    if (inGame) {
      msg = " is playing a game.";
    } else {
      msg = " has left the chatroom.";
    }
    msg = username + msg;
    chat_server.broadcastMessage(msg);
    chat_server.remove_user(username);
  }
}

Sequence AddUser(TrueFalse inGame) {
  User.doNothing {}
  UserHelper.sendServer {
    Text msg;
    if (inGame) {
      msg = " is back from a game.";
    } else {
      msg = " has entered the chatroom.";
    }
    msg = username + msg;
    chat_server.broadcastMessage(msg);
    chat_server.add_user(username, self);
  }
}

Sequence SendPrivate(Text receiver, Text msg) {
  TrueFalse message_sent;
  User.doNothing{}
  UserHelper.sendMessage {
    msg = 'private message from ' + username + ': ' + msg;
    message_sent = chat_server.send_message(receiver, msg);
  }
  User.checkSent {
    if (not message_sent) {
      msg = receiver + ' does not exist in chat.';
      extCopy msg to message;
    }
  }
}

Sequence SendMessage(Text msg) {
  User.send {
  }
  UserHelper.updateUsers{
    chat_server.broadcastMessage(msg);
  }
}

Sequence DisplayMessage(Text msg) {
  UserHelper.doNothing{}
  User.printMessage {
    extCopy msg to message;
  }
}

Sequence PrintUsers() {
  List(element: Text) users_list;

  User.doNothing{}

  UserHelper.get_list {
    users_list = chat_server.get_users();
  }

  User.print_list {
    extCopy 'Users in chat:' to message;
    for (Text user in users_list) {
      extCopy user to message;
    }
  }

}

User {
  External Text message;
  onCreate(Text name, External Text gui_str) {
    username = name;
    extAssign gui_str to message;
  }
  Public Function send_message(Text msg) {
    SendMessage(msg);
  }
  Public Function add_to_server(TrueFalse inGame) {
    AddUser(inGame);
  }

  Public Function quit(TrueFalse inGame) {
    Quit(inGame);
  }

  Public Function private_message(Text receiver, Text msg) {
    SendPrivate(receiver, msg);
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
  Public Function get_new_message(Text msg) returns Nothing {
    DisplayMessage(msg);
  }
}
