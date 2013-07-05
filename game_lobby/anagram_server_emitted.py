# Waldo emitted file


def AnagramServer (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _AnagramServer (_waldo_classes["Endpoint"]):
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
                '0__players',self._waldo_classes["WaldoMapVariable"](  # the type of waldo variable to create
                '0__players', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '1__player_scores',self._waldo_classes["WaldoMapVariable"](  # the type of waldo variable to create
                '1__player_scores', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '2__solutions',self._waldo_classes["WaldoListVariable"](  # the type of waldo variable to create
                '2__solutions', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '3__anagram',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '3__anagram', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '4__game_in_session',self._waldo_classes["WaldoTrueFalseVariable"](  # the type of waldo variable to create
                '4__game_in_session', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
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
                _to_return = self._onCreate(_root_event,_ctx ,[])
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

        def _onCreate(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            _tmp0 = False 
            if not _context.assign(_context.global_store.get_var_if_exists("4__game_in_session"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def set_solution(self,init_anagram,solution):

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
                _to_return = self._endpoint_func_call_prefix__waldo__set_solution(_root_event,_ctx ,init_anagram,solution,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__set_solution(self,_active_event,_context,init_anagram,solution,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                init_anagram = _context.turn_into_waldo_var_if_was_var(init_anagram,True,_active_event,self._host_uuid,False,False)
                solution = _context.turn_into_waldo_var_if_was_var(solution,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                init_anagram = _context.turn_into_waldo_var_if_was_var(init_anagram,True,_active_event,self._host_uuid,False,False)
                solution = _context.turn_into_waldo_var_if_was_var(solution,False,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = init_anagram
            if not _context.assign(_context.global_store.get_var_if_exists("3__anagram"),_tmp0,_active_event):
                pass

            _tmp0 = solution
            if not _context.assign(_context.global_store.get_var_if_exists("2__solutions"),_tmp0,_active_event):
                pass



        def start_game(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__start_game(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__start_game(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            _tmp0 = True 
            if not _context.assign(_context.global_store.get_var_if_exists("4__game_in_session"),_tmp0,_active_event):
                pass

            username = ""
            for _secret_waldo_for_iter____username in _context.get_for_iter(_context.global_store.get_var_if_exists("0__players"),_active_event):
                username = _context.write_val(username,_secret_waldo_for_iter____username,_active_event)
                _tmp0 = 0 
                _context.assign_on_key(_context.global_store.get_var_if_exists("1__player_scores"),username,_tmp0, _active_event)

                _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__players").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event),"get_new_message",'Game has started.' ,)

                pass



        def get_game_status(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__get_game_status(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__get_game_status(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("4__game_in_session") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("4__game_in_session"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("4__game_in_session"))




        def return_anagram(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__return_anagram(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__return_anagram(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("3__anagram") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("3__anagram"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("3__anagram"))




        def return_solutions(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__return_solutions(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__return_solutions(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("2__solutions") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("2__solutions"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("2__solutions"))




        def get_player_count(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__get_player_count(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__get_player_count(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.handle_len(_context.global_store.get_var_if_exists("0__players"),_active_event) if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.handle_len(_context.global_store.get_var_if_exists("0__players"),_active_event),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.handle_len(_context.global_store.get_var_if_exists("0__players"),_active_event))




        def get_scores(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__get_scores(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__get_scores(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__player_scores") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("1__player_scores"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__player_scores"))




        def add_score(self,username,points):

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
                _to_return = self._endpoint_func_call_prefix__waldo__add_score(_root_event,_ctx ,username,points,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__add_score(self,_active_event,_context,username,points,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                points = _context.turn_into_waldo_var_if_was_var(points,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                points = _context.turn_into_waldo_var_if_was_var(points,True,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = (_context.get_val_if_waldo(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event) + _context.get_val_if_waldo(points,_active_event))
            _context.assign_on_key(_context.global_store.get_var_if_exists("1__player_scores"),username,_tmp0, _active_event)


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)) if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)))




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
            _context.assign_on_key(_context.global_store.get_var_if_exists("0__players"),username,_tmp0, _active_event)



        def get_score(self,username):

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
                _to_return = self._endpoint_func_call_prefix__waldo__get_score(_root_event,_ctx ,username,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__get_score(self,_active_event,_context,username,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)) if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)))




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

            _context.global_store.get_var_if_exists("0__players").get_val(_active_event).del_key_called(_active_event,_context.get_val_if_waldo(username,_active_event))
            _context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).del_key_called(_active_event,_context.get_val_if_waldo(username,_active_event))


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
            for _secret_waldo_for_iter____username in _context.get_for_iter(_context.global_store.get_var_if_exists("0__players"),_active_event):
                username = _context.write_val(username,_secret_waldo_for_iter____username,_active_event)
                _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__players").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event),"get_new_message",message,)

                pass



        def end_game(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__end_game(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__end_game(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            _tmp0 = False 
            if not _context.assign(_context.global_store.get_var_if_exists("4__game_in_session"),_tmp0,_active_event):
                pass

            self._endpoint_func_call_prefix__waldo__broadcastMessage(_active_event,_context,'Game Over.' ,)
            username = ""
            for _secret_waldo_for_iter____username in _context.get_for_iter(_context.global_store.get_var_if_exists("1__player_scores"),_active_event):
                username = _context.write_val(username,_secret_waldo_for_iter____username,_active_event)
                score = _context.get_val_if_waldo((_context.get_val_if_waldo(username,_active_event) + _context.get_val_if_waldo((_context.get_val_if_waldo(' - ' ,_active_event) + _context.get_val_if_waldo(_context.to_text(_context.global_store.get_var_if_exists("1__player_scores").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event),_active_event)),_active_event)),_active_event)
                self._endpoint_func_call_prefix__waldo__broadcastMessage(_active_event,_context,score,)

                pass

            self._endpoint_func_call_prefix__waldo__broadcastMessage(_active_event,_context,'Press ENTER to continue.' ,)
            _tmp0 = self._waldo_classes["WaldoSingleThreadMapVariable"]("garbage_name",
                self._host_uuid,
                False,
                {})
            if not _context.assign(_context.global_store.get_var_if_exists("0__players"),_tmp0,_active_event):
                pass

            _tmp0 = self._waldo_classes["WaldoSingleThreadMapVariable"]("garbage_name",
                self._host_uuid,
                False,
                {})
            if not _context.assign(_context.global_store.get_var_if_exists("1__player_scores"),_tmp0,_active_event):
                pass


        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return _AnagramServer(_waldo_classes,_host_uuid,_conn_obj,*args)
def _AnagramServer (_waldo_classes,_host_uuid,_conn_obj,*args):
    class __AnagramServer (_waldo_classes["Endpoint"]):
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

    return __AnagramServer(_waldo_classes,_host_uuid,_conn_obj,*args)
