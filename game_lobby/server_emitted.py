# Waldo emitted file


def Server (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _Server (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj):

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
                '0__users',self._waldo_classes["WaldoMapVariable"](  # the type of waldo variable to create
                '0__users', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._waldo_classes["Endpoint"].__init__(self,_waldo_classes,_host_uuid,_conn_obj,self._global_var_store)



            # local endpoint's initialization has succeeded, tell other side that
            # we're done initializing.
            self._this_side_ready()


        ### OnCreate method

        # no oncreate defined to emit method for 
        ### USER DEFINED METHODS ###

        def add_user(self,username,pt):

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
                _to_return = self._endpoint_func_call_prefix__waldo__add_user(_root_event,_ctx ,username,pt,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__add_user(self,_active_event,_context,username,pt,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                pt = _context.turn_into_waldo_var_if_was_var(pt,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                pt = _context.turn_into_waldo_var_if_was_var(pt,True,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = pt
            _context.assign_on_key(_context.global_store.get_var_if_exists("0__users"),username,_tmp0, _active_event)



        def remove_user(self,username):

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
                _to_return = self._endpoint_func_call_prefix__waldo__remove_user(_root_event,_ctx ,username,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__remove_user(self,_active_event,_context,username,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)

                pass

            _context.global_store.get_var_if_exists("0__users").get_val(_active_event).del_key_called(_active_event,_context.get_val_if_waldo(username,_active_event))


        def broadcastMessage(self,message):

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
                _to_return = self._endpoint_func_call_prefix__waldo__broadcastMessage(_root_event,_ctx ,message,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__broadcastMessage(self,_active_event,_context,message,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            username = ""
            for _secret_waldo_for_iter____username in _context.get_for_iter(_context.global_store.get_var_if_exists("0__users"),_active_event):
                username = _context.write_val(username,_secret_waldo_for_iter____username,_active_event)
                _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__users").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event),"get_new_message",message,)

                pass



        def send_message(self,receiver,message):

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
                _to_return = self._endpoint_func_call_prefix__waldo__send_message(_root_event,_ctx ,receiver,message,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__send_message(self,_active_event,_context,receiver,message,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                receiver = _context.turn_into_waldo_var_if_was_var(receiver,True,_active_event,self._host_uuid,False,False)
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                receiver = _context.turn_into_waldo_var_if_was_var(receiver,True,_active_event,self._host_uuid,False,False)
                message = _context.turn_into_waldo_var_if_was_var(message,True,_active_event,self._host_uuid,False,False)

                pass

            if _context.get_val_if_waldo(( not ( _context.get_val_if_waldo(_context.handle_in_check(receiver,_context.global_store.get_var_if_exists("0__users"),_active_event),_active_event) )),_active_event):

                if _returning_to_public_ext_array != None:
                    # must de-waldo-ify objects before passing back
                    return _context.flatten_into_single_return_tuple(False  if 0 in _returning_to_public_ext_array else _context.de_waldoify(False ,_active_event))


                # otherwise, use regular return mechanism... do not de-waldo-ify
                return _context.flatten_into_single_return_tuple(False )



                pass


            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__users").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(receiver,_active_event)),_active_event),"get_new_message",message,)

            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(True  if 0 in _returning_to_public_ext_array else _context.de_waldoify(True ,_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(True )




        def get_users(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__get_users(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__get_users(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            users_list = self._waldo_classes["WaldoSingleThreadListVariable"](  # the type of waldo variable to create
                '10__users_list', # variable's name
                self._host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            )
            username = ""
            for _secret_waldo_for_iter____username in _context.get_for_iter(_context.global_store.get_var_if_exists("0__users"),_active_event):
                username = _context.write_val(username,_secret_waldo_for_iter____username,_active_event)
                users_list.get_val(_active_event).append_val(_active_event,_context.get_val_if_waldo(username,_active_event))

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(users_list if 0 in _returning_to_public_ext_array else _context.de_waldoify(users_list,_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(users_list)



        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return _Server(_waldo_classes,_host_uuid,_conn_obj,*args)
def _Server (_waldo_classes,_host_uuid,_conn_obj,*args):
    class __Server (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj):

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

            self._waldo_classes["Endpoint"].__init__(self,_waldo_classes,_host_uuid,_conn_obj,self._global_var_store)



            # local endpoint's initialization has succeeded, tell other side that
            # we're done initializing.
            self._this_side_ready()


        ### OnCreate method

        # no oncreate defined to emit method for 
        ### USER DEFINED METHODS ###
        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return __Server(_waldo_classes,_host_uuid,_conn_obj,*args)
