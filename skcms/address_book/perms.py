# # coding=utf-8
#
# from permission.logics import AuthorPermissionLogic
# from permission.logics import CollaboratorsPermissionLogic
# from permission.logics.base import PermissionLogic
#
#
# PERMISSION_LOGICS = (
#     # ("address_book.Person", AuthorPermissionLogic(
#     #     field_name='user',
#     #     ),
#     # ),
#     # ("address_book.Person", CollaboratorsPermissionLogic(
#     #     field_name='collaborators',
#     #     any_permission=False,
#     #     change_permission=True,
#     #     delete_permission=False,)
#     #  ),
# )
#
#
# class AddressBookPermissionLogic(PermissionLogic):
#     """
#     Permission logic of Event model which for
#     - `address_book.add`
#     - `address_book.change`
#     - `address_book.delete`
#     - `address_book.attend`
#     - `address_book.quit`
#     """
#
#     def has_perm(self, user_obj, perm, obj=None):
#         """
#         Check if user have a specified event permissions (of obj)
#         """
#         # anonymous use has no permissions
#         if not user_obj.is_authenticated():
#             return False
#         # filter interest permissions
#         if perm not in ('address_book.add',
#                         'address_book.change',
#                         'address_book.delete',
#                         'address_book.attend',
#                         'address_book.quit'):
#             return False
#         if obj is None:
#             # generally, authenticated user have attend/quit permission
#             if perm in ('address_book.attend', 'address_book.quit'):
#                 return True
#             # seele, nerv, children have an add permission
#             permissions = ('address_book.add',
#                            'address_book.change',
#                            'address_book.delete')
#             roles = ('seele', 'nerv', 'children')
#             if perm in permissions and user_obj.role in roles:
#                 # seele, nerv, children have permissions of add, change, event
#                 # generally
#                 return True
#             return False
