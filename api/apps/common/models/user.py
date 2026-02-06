""" class UserAccount(PermissionsMixin, VersionedCoreModel, AbstractBaseUser):
    email = models.EmailField(verbose_name=_("Email"), max_length=255, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )

    permissions = ArrayField(
        models.CharField(choices=Permissions.choices), blank=True, default=list
    )

    def __str__(self):
        return self.email
 """