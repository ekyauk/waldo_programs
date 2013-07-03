# Waldo emitted file


def User (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _User (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,name,prntmsg):

            # a little ugly in that need to pre-initialize _host_uuid, because
            # code used for initializing variable store may rely on it.  (Eg., if
            # initializing nested lists.)
            self._waldo_classes = _waldo_classes
            self._host_uuid = _host_uuid
            self._global_var_store = self._waldo_classes["VariableStore"](_host_uuid)
            _active_event = None
            _context = self._waldo_classes["ExecutingEventContext"](
                self._global_var_store,
                # not using sequence local store
                self._waldo_classes["VariableStore"](_host_uuid))

            self._global_var_store.add_var(
                '1__print_message',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '1__print_message', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ).set_external_args_array([]))

            self._global_var_store.add_var(
                '0__username',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '0__username', # variable's name
                _host_uuid, # host uuid var name
                True,  # if peered, True, otherwise, False
                
            ))

            self._waldo_classes["Endpoint"].__init__(self,_waldo_classes,_host_uuid,_conn_obj,self._global_var_store)


            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._onCreate(_root_event,_ctx ,name,prntmsg,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done

                    # local endpoint's initialization has succeeded, tell other side that
                    # we're done initializing.
                    self._this_side_ready()

                    return _to_return

                
            # local endpoint's initialization has succeeded, tell other side that
            # we're done initializing.
            self._this_side_ready()


        ### OnCreate method

        def _onCreate(self,_active_event,_context,name,prntmsg,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                name = _context.turn_into_waldo_var_if_was_var(name,True,_active_event,self._host_uuid,False,False)
                prntmsg = _context.func_turn_into_waldo_var(prntmsg,True,_active_event,self._host_uuid,False,[],False)

                pass

            else:
                name = _context.turn_into_waldo_var_if_was_var(name,True,_active_event,self._host_uuid,False,False)
                prntmsg = _context.func_turn_into_waldo_var(prntmsg,True,_active_event,self._host_uuid,False,[],False)

                pass

            _tmp0 = name
            if not _context.assign(_context.global_store.get_var_if_exists("0__username"),_tmp0,_active_event):
                pass

            _tmp0 = prntmsg
            if not _context.assign(_context.global_store.get_var_if_exists("1__print_message"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def send_message(self,message):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__send_message(_root_event,_ctx ,message,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__send_message(self,_active_event,_context,message,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__SendMessage(_active_event,_context,message,) if _context.set_msg_send_initialized_bit_false() else None)


        def add_to_server(self):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__add_to_server(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__add_to_server(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__AddUser(_active_event,_context,) if _context.set_msg_send_initialized_bit_false() else None)


        def quit(self):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__quit(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__quit(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__Quit(_active_event,_context,) if _context.set_msg_send_initialized_bit_false() else None)


        def private_message(self,receiver,message):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__private_message(_root_event,_ctx ,receiver,message,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__private_message(self,_active_event,_context,receiver,message,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                receiver = _context.turn_into_waldo_var_if_was_var(receiver,True,_active_event,self._host_uuid,False,False)
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                receiver = _context.turn_into_waldo_var_if_was_var(receiver,True,_active_event,self._host_uuid,False,False)
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__SendPrivate(_active_event,_context,receiver,message,) if _context.set_msg_send_initialized_bit_false() else None)


        def print_users(self):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__print_users(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__print_users(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__PrintUsers(_active_event,_context,) if _context.set_msg_send_initialized_bit_false() else None)

        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__Quit(self,_active_event,_context,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    pass

                else:

                    pass


                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'notify',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return 

        def _partner_endpoint_msg_func_call_prefix__waldo__AddUser(self,_active_event,_context,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    pass

                else:

                    pass


                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'sendServer',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return 

        def _partner_endpoint_msg_func_call_prefix__waldo__SendPrivate(self,_active_event,_context,receiver=None,message=None,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    _context.sequence_local_store.add_var(
                        "21__receiver", _context.convert_for_seq_local(receiver,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "22__message", _context.convert_for_seq_local(message,_active_event,self._host_uuid)
                    )

                    pass

                else:

                    _context.sequence_local_store.add_var(
                        "21__receiver", _context.convert_for_seq_local(receiver,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "22__message", _context.convert_for_seq_local(message,_active_event,self._host_uuid)
                    )

                    pass

                message_sent = False
                _context.sequence_local_store.add_var(
                    "20__message_sent",_context.convert_for_seq_local(message_sent,_active_event,self._host_uuid))

                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'sendMessage',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return 

        def _partner_endpoint_msg_func_call_prefix__waldo__SendMessage(self,_active_event,_context,message=None,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    _context.sequence_local_store.add_var(
                        "26__message", _context.convert_for_seq_local(message,_active_event,self._host_uuid)
                    )

                    pass

                else:

                    _context.sequence_local_store.add_var(
                        "26__message", _context.convert_for_seq_local(message,_active_event,self._host_uuid)
                    )

                    pass


                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'updateUsers',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return 

        def _partner_endpoint_msg_func_call_prefix__waldo__PrintUsers(self,_active_event,_context,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    pass

                else:

                    pass

                users_list = self._waldo_classes["WaldoSingleThreadListVariable"](  # the type of waldo variable to create
                    '31__users_list', # variable's name
                    self._host_uuid, # host uuid var name
                    False,  # if peered, True, otherwise, False
                    
                )
                _context.sequence_local_store.add_var(
                    "31__users_list",_context.convert_for_seq_local(users_list,_active_event,self._host_uuid))

                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'get_list',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return 

        ### User-defined message receive blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__checkSent(self,_active_event,_context,_returning_to_public_ext_array=None):

            if _context.get_val_if_waldo(( not ( _context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("20__message_sent"),_active_event) )),_active_event):
                _tmp0 = (_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("21__receiver"),_active_event) + _context.get_val_if_waldo(' does not exist in chat.' ,_active_event))
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("22__message"),_tmp0,_active_event):
                    pass

                _context.call_func_obj(_active_event,_context.global_store.get_var_if_exists("1__print_message"),_context.sequence_local_store.get_var_if_exists("22__message"))

                pass





            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__printMessage(self,_active_event,_context,_returning_to_public_ext_array=None):

            _context.call_func_obj(_active_event,_context.global_store.get_var_if_exists("1__print_message"),_context.sequence_local_store.get_var_if_exists("28__message"))



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__print_list(self,_active_event,_context,_returning_to_public_ext_array=None):

            _context.call_func_obj(_active_event,_context.global_store.get_var_if_exists("1__print_message"),'Users in chat:' )
            _context.call_func_obj(_active_event,_context.global_store.get_var_if_exists("1__print_message"),'' )
            user = ""
            for _secret_waldo_for_iter____user in _context.get_for_iter(_context.sequence_local_store.get_var_if_exists("31__users_list"),_active_event):
                user = _context.write_val(user,_secret_waldo_for_iter____user,_active_event)
                _context.call_func_obj(_active_event,_context.global_store.get_var_if_exists("1__print_message"),user)

                pass

            _context.call_func_obj(_active_event,_context.global_store.get_var_if_exists("1__print_message"),'' )



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


    return _User(_waldo_classes,_host_uuid,_conn_obj,*args)
def UserHelper (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _UserHelper (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,server):

            # a little ugly in that need to pre-initialize _host_uuid, because
            # code used for initializing variable store may rely on it.  (Eg., if
            # initializing nested lists.)
            self._waldo_classes = _waldo_classes
            self._host_uuid = _host_uuid
            self._global_var_store = self._waldo_classes["VariableStore"](_host_uuid)
            _active_event = None
            _context = self._waldo_classes["ExecutingEventContext"](
                self._global_var_store,
                # not using sequence local store
                self._waldo_classes["VariableStore"](_host_uuid))

            self._global_var_store.add_var(
                '12__chat_server',self._waldo_classes["WaldoEndpointVariable"](  # the type of waldo variable to create
                '12__chat_server', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '0__username',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '0__username', # variable's name
                _host_uuid, # host uuid var name
                True,  # if peered, True, otherwise, False
                
            ))

            self._waldo_classes["Endpoint"].__init__(self,_waldo_classes,_host_uuid,_conn_obj,self._global_var_store)


            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._onCreate(_root_event,_ctx ,server,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done

                    # local endpoint's initialization has succeeded, tell other side that
                    # we're done initializing.
                    self._this_side_ready()

                    return _to_return

                
            # local endpoint's initialization has succeeded, tell other side that
            # we're done initializing.
            self._this_side_ready()


        ### OnCreate method

        def _onCreate(self,_active_event,_context,server,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                server = _context.turn_into_waldo_var_if_was_var(server,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                server = _context.turn_into_waldo_var_if_was_var(server,True,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = server
            if not _context.assign(_context.global_store.get_var_if_exists("12__chat_server"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def get_new_message(self,message):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__get_new_message(_root_event,_ctx ,message,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__get_new_message(self,_active_event,_context,message,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__DisplayMessage(_active_event,_context,message,) if _context.set_msg_send_initialized_bit_false() else None)

        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__DisplayMessage(self,_active_event,_context,message=None,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    _context.sequence_local_store.add_var(
                        "28__message", _context.convert_for_seq_local(message,_active_event,self._host_uuid)
                    )

                    pass

                else:

                    _context.sequence_local_store.add_var(
                        "28__message", _context.convert_for_seq_local(message,_active_event,self._host_uuid)
                    )

                    pass


                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'printMessage',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return 

        ### User-defined message receive blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__notify(self,_active_event,_context,_returning_to_public_ext_array=None):

            message = _context.get_val_if_waldo((_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__username"),_active_event) + _context.get_val_if_waldo(' has left the chatroom.' ,_active_event)),_active_event)
            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("12__chat_server"),_active_event),"broadcastMessage",message,)
            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("12__chat_server"),_active_event),"remove_user",_context.global_store.get_var_if_exists("0__username"),)



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__sendServer(self,_active_event,_context,_returning_to_public_ext_array=None):

            message = _context.get_val_if_waldo((_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__username"),_active_event) + _context.get_val_if_waldo(' has entered the chatroom.' ,_active_event)),_active_event)
            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("12__chat_server"),_active_event),"broadcastMessage",message,)
            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("12__chat_server"),_active_event),"add_user",_context.global_store.get_var_if_exists("0__username"),self,)



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__sendMessage(self,_active_event,_context,_returning_to_public_ext_array=None):

            _tmp0 = (_context.get_val_if_waldo('private message from ' ,_active_event) + _context.get_val_if_waldo((_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__username"),_active_event) + _context.get_val_if_waldo((_context.get_val_if_waldo(': ' ,_active_event) + _context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("22__message"),_active_event)),_active_event)),_active_event))
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("22__message"),_tmp0,_active_event):
                pass

            _tmp0 = _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("12__chat_server"),_active_event),"send_message",_context.sequence_local_store.get_var_if_exists("21__receiver"),_context.sequence_local_store.get_var_if_exists("22__message"),)
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("20__message_sent"),_tmp0,_active_event):
                pass




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,"_partner_endpoint_msg_func_call_prefix__waldo__checkSent",_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if "_partner_endpoint_msg_func_call_prefix__waldo__checkSent" != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__updateUsers(self,_active_event,_context,_returning_to_public_ext_array=None):

            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("12__chat_server"),_active_event),"broadcastMessage",_context.sequence_local_store.get_var_if_exists("26__message"),)



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__get_list(self,_active_event,_context,_returning_to_public_ext_array=None):

            _tmp0 = _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("12__chat_server"),_active_event),"get_users",)
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("31__users_list"),_tmp0,_active_event):
                pass




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,"_partner_endpoint_msg_func_call_prefix__waldo__print_list",_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if "_partner_endpoint_msg_func_call_prefix__waldo__print_list" != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


    return _UserHelper(_waldo_classes,_host_uuid,_conn_obj,*args)
