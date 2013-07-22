# Waldo emitted file


def PasswordServer (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _PasswordServer (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,existing_users,save):

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
                '0__database',self._waldo_classes["WaldoMapVariable"](  # the type of waldo variable to create
                '0__database', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '1__users',self._waldo_classes["WaldoMapVariable"](  # the type of waldo variable to create
                '1__users', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '2__save_database',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '2__save_database', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ).set_external_args_array([]))

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
                try:
                    _to_return = self._onCreate(_root_event,_ctx ,existing_users,save,[])
                except self._waldo_classes["BackoutException"]:
                    pass

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

        def _onCreate(self,_active_event,_context,existing_users,save,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                existing_users = _context.turn_into_waldo_var_if_was_var(existing_users,True,_active_event,self._host_uuid,False,False)
                save = _context.func_turn_into_waldo_var(save,True,_active_event,self._host_uuid,False,[],False)

                pass

            else:
                existing_users = _context.turn_into_waldo_var_if_was_var(existing_users,False,_active_event,self._host_uuid,False,False)
                save = _context.func_turn_into_waldo_var(save,True,_active_event,self._host_uuid,False,[],False)

                pass

            _tmp0 = existing_users
            if not _context.assign(_context.global_store.get_var_if_exists("0__database"),_tmp0,_active_event):
                pass

            _tmp0 = save
            if not _context.assign(_context.global_store.get_var_if_exists("2__save_database"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def close(self):

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
                try:
                    _to_return = self._endpoint_func_call_prefix__waldo__close(_root_event,_ctx ,[])
                except self._waldo_classes["BackoutException"]:
                    pass

                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__close(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            _context.call_func_obj(_active_event,_context.global_store.get_var_if_exists("2__save_database"),_context.global_store.get_var_if_exists("0__database"))


        def register_user(self,username,password):

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
                try:
                    _to_return = self._endpoint_func_call_prefix__waldo__register_user(_root_event,_ctx ,username,password,[])
                except self._waldo_classes["BackoutException"]:
                    pass

                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__register_user(self,_active_event,_context,username,password,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                password = _context.turn_into_waldo_var_if_was_var(password,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                password = _context.turn_into_waldo_var_if_was_var(password,True,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = password
            _context.assign_on_key(_context.global_store.get_var_if_exists("0__database"),username,_tmp0, _active_event)



        def check_user(self,username):

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
                try:
                    _to_return = self._endpoint_func_call_prefix__waldo__check_user(_root_event,_ctx ,username,[])
                except self._waldo_classes["BackoutException"]:
                    pass

                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__check_user(self,_active_event,_context,username,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.handle_in_check(username,_context.global_store.get_var_if_exists("0__database"),_active_event) if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.handle_in_check(username,_context.global_store.get_var_if_exists("0__database"),_active_event),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.handle_in_check(username,_context.global_store.get_var_if_exists("0__database"),_active_event))




        def check_password(self,username,password):

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
                try:
                    _to_return = self._endpoint_func_call_prefix__waldo__check_password(_root_event,_ctx ,username,password,[])
                except self._waldo_classes["BackoutException"]:
                    pass

                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__check_password(self,_active_event,_context,username,password,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                password = _context.turn_into_waldo_var_if_was_var(password,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                username = _context.turn_into_waldo_var_if_was_var(username,True,_active_event,self._host_uuid,False,False)
                password = _context.turn_into_waldo_var_if_was_var(password,True,_active_event,self._host_uuid,False,False)

                pass

            if _context.get_val_if_waldo(_context.handle_in_check(username,_context.global_store.get_var_if_exists("0__database"),_active_event),_active_event):

                if _returning_to_public_ext_array != None:
                    # must de-waldo-ify objects before passing back
                    return _context.flatten_into_single_return_tuple((_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__database").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event) == _context.get_val_if_waldo(password,_active_event)) if 0 in _returning_to_public_ext_array else _context.de_waldoify((_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__database").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event) == _context.get_val_if_waldo(password,_active_event)),_active_event))


                # otherwise, use regular return mechanism... do not de-waldo-ify
                return _context.flatten_into_single_return_tuple((_context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__database").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(username,_active_event)),_active_event) == _context.get_val_if_waldo(password,_active_event)))



                pass



            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(False  if 0 in _returning_to_public_ext_array else _context.de_waldoify(False ,_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(False )



        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return _PasswordServer(_waldo_classes,_host_uuid,_conn_obj,*args)
def _PasswordServer (_waldo_classes,_host_uuid,_conn_obj,*args):
    class __PasswordServer (_waldo_classes["Endpoint"]):
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

    return __PasswordServer(_waldo_classes,_host_uuid,_conn_obj,*args)
