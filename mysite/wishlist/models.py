from django.db import models


####################
#    User Class    #
####################

class User(models.Model):
    """
    Model for a user.
    """

    ###################
    #    Variables    #
    ###################

    username = models.CharField(max_length=20, primary_key=True)
    firstName = models.CharField(verbose_name="first name", max_length=50)
    lastName = models.CharField(verbose_name="last name", max_length=50)


    #################
    #    Methods    #
    #################

    def __str__(self):
        return "User <{}>".format(self.username)


########################
#    Wishlist Class    #
########################

class Wishlist(models.Model):
    """
    Model for a user's wishlist.
    """

    ###################
    #    Variables    #
    ###################

    #django automatically adds id as pkey

    #each wishlist is associated with a user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="wishlist owner")


    #################
    #    Methods    #
    #################

    def __str__(self):
        return "Wishlist owned by {} (id={})".format(self.owner, self.id)


#############################
#    WishlistEntry Class    #
#############################

class WishlistEntry(models.Model):
    """
    Model for a single entry in a wishlist.
    """

    ###################
    #    Variables    #
    ###################


    #associates the entry with a specific list
    wishlistId = models.ForeignKey(Wishlist, on_delete=models.CASCADE, verbose_name="wishlist id")

    itemName = models.CharField(verbose_name="item name", max_length=200)
    linkToItem = models.TextField(verbose_name="link to item", blank=True) #optional link to a webpage for the item

    #true if someone has claimed the item
    itemIsClaimed = models.BooleanField(verbose_name="item has been claimed", default=False)


    #################
    #    Methods    #
    #################

    def __str__(self):
        return "Entry for {} (wishlistId={})".format(self.itemName, self.wishlistId)