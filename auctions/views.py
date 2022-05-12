from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Max
from .forms import *
from .models import User, Listing, Comment, Bid, Category


def index(request):
    active_listings = Listing.objects.filter(isActive=True)
    ## user has clicked on a category
    if request.method == "POST":
      
        categoryId = request.POST['category']
        print("Hi")
        print(int(categoryId))
        # get the category from the posted data
        category_selected = Category.objects.get(pk=categoryId)
        active_listings = Listing.objects.filter(category_id=category_selected.id, isActive=True)
        # active_listings = Listing.objects.filter(category.id=categoryId)
    #    active_listings_in_category.objects.filter()

    return render(request, "auctions/index.html", {
        "active_listings": active_listings
        # Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    ### check if the method is post, if it is, then grab the information
    ### and save it to the database and then render the user to the 
    ### index (main page with all listings)
    # categories = Category.objects.all()
   
    if request.method == "POST":
        title = request.POST['listing_title']
        user = request.user 
        # password = request.POST["password"]
        description = request.POST['description']
        bid = request.POST['bid']
        print("Value is2 :")
        print(bid=="")
        if bid == "" or bid == None:
            print("Value is:")
            print(bid)
            bid = 0.01
        url = request.POST['image_url']
        categoryText = request.POST['category']
        category = Category.objects.get(categoryText=categoryText)
        # startBid = Bid.objects.get(bid=bid)
        bid = Bid(bid=bid, owner=user)
        bid.save()
        listing = Listing(listingTitle=title, description=description, currentBid=bid.bid, imageUrl=url, listingOwner=user, category=category, bid=bid)
        print("TEST: ")
        # print(startBid.bid)
        listing.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/create_listing.html")

# Changed from upload_image
def add_listing(request):
    
    form = AddListingForm(request.POST, request.FILES)
    if request.method == "POST":
        # form = ImageForm(request.POST, request.FILES)
        user = request.user 
        # check if the form is valid
        if form.is_valid():
            startingBid = form.cleaned_data.get("currentBid")
            print(startingBid)
            if startingBid == "" or startingBid == None:
                # startingBid = 0.01
                return render(request, "auctions/add_listing.html", {
                    "startBid": False,
                    "message": "Please enter a starting bid",
                    "form": form
                })
            listing = form.save()
            listing.listingOwner = user
          
            # bid = Bid(bid=startingBid, owner=user)
            # bid.save()
            # listing.bid = bid
            listing.currentBid = startingBid
            listing.save()
           
           
            print("Success")
            # print(bid.bid)
            # print(bid.owner)
            # print(listing.bid)
            # print(listing.id)
            
            # print("")
            # print(listing.listingOwner)
            # print(listing.category)
            # return redirect("Success")
            # return render(request, "auctions/index.html")
            return HttpResponseRedirect(reverse("index"))
        else:
            form = AddListingForm()
            return render(request, "auctions/add_listing.html", {
                'form' : form
            })
    return render(request, "auctions/add_listing.html", {
        "form" : form
    })

def success(request):
    return HttpResponse('successfully uploaded')  
    

def view_listing(request, listing_id):
    ## check if user is logged in
    listing = Listing.objects.get(pk=listing_id)
    comments = Comment.objects.all().filter(listing=listing)
    # get all bids for this listing
    # bids = Bid.objects.all().filter(listing=listing)
    # find the highest Bid

    # Is the person viewing the listing the owner 
    if request.user == listing.listingOwner:
        isOwner = True
    else:
        isOwner = False
    return render(request, "auctions/display_listing.html", {
        "listing": listing,
        "isOwner": isOwner,
        "comments": comments
    })

def close_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.isActive = False
    # save/update the database
    listing.save()
    # return render(request, "auctions/index.html")
    # return HttpResponseRedirect(reverse("view_listing", args=(listing_id,)))
    return HttpResponseRedirect(reverse("index"))

def add_comment(request, listing_id):
    user = request.user 
    ## check if user is signed in
    if user.is_authenticated:
        if request.method == "POST":
            listing = Listing.objects.get(pk=listing_id)
            comment = request.POST['comment']
            ## request.user shu had
            user = request.user 
            comment = Comment(content=comment, owner=user, listing=listing)
            comment.save()
            ## Delete after
            # make sure comment is not empty (there is text)
            if not comment:
            # return render(request, "auctions/index.html")
                return HttpResponseRedirect(reverse("view_listing", args=(listing_id,)))
            else:
                # return render(request, "auctions/index.html")
                return HttpResponseRedirect(reverse("view_listing", args=(listing_id,)))
    else:
        return HttpResponseRedirect(reverse("view_listing", args=(listing_id,)))  
    
def view_categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/category.html", {
        "categories": categories

    })

def submit_bid(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    # myBid = Bid.objects.get(bid=listing.currentBid)
    bidPlaced = True
    bidSuccessful =  True
    if request.method == "POST":
        
        newBid = request.POST['bid']
        if newBid == '' or newBid == None:
            bidPlaced = False
            # return HttpResponseRedirect(reverse("view_listing", args=(listing_id,)))
            return render(request,"auctions/display_listing.html",{
                "listing":listing,
                "message":"Please submit a valid bid that is at least larger than the latest bid!",
                "bidPlaced": bidPlaced,
            })
        print(float(newBid))
        print(listing.currentBid)
        # the new bid is larger than the previus bid
        if float(newBid) > listing.currentBid:
            user = request.user
            updatedBid = Bid(bid=newBid, owner=user)
            updatedBid.save()
            listing.bid = updatedBid
            listing.currentBid = newBid
            listing.save()
            # bidPlaced = True
            return render(request,"auctions/display_listing.html",{
                "listing":listing,
                "message":"You've successfully submitted your bid!",
                "bidSuccessful": bidSuccessful,
            })
        else:
            bidSuccessful = False
            # the bid is less than the previous so present an error message
            # return HttpResponseRedirect(reverse("wiki:entry", kwargs={"title": entryTitle}))
            return render(request,"auctions/display_listing.html",{
                "listing":listing,
                "message":"The bid you've placed is not larger than the latest bid.",
                "bidSuccessful": bidSuccessful,
            })
            return HttpResponseRedirect(reverse("view_listing", args=(listing_id,)))


    return HttpResponseRedirect(reverse("view_listing", args=(listing_id,)))

## TODO ###
def edit_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    form = AddListingForm(request.POST, request.FILES, instance=listing)
    print("try here")
    print(listing.listingTitle)
    #### TEST
    if request.method == "POST":
        if form.is_valid():
            print("Post Method called and form is valid")
            listing = form.save()
            listing.save()
            print("Category Text")
            print(listing.category.categoryText)
            return HttpResponseRedirect(reverse("view_listing", args=(listing.id,)))
        else:
            pass
    else:
        # Method is GET
    #     print("get method called")
    #     form.fields['listingTitle'].initial = listing.listingTitle
    #     form.fields['description'].initial = listing.description
    #     form.fields['currentBid'].initial = listing.currentBid
    #     # form.fields['currentBid'].widget = forms.HiddenInput()
    #     form.fields['category'].initial = listing.category
    #      data = {'pres_clinic' : 'value', 'bcg_scar' : 'value', 'mantoux_register' : 'value'}
        # print("We're here")
        data = {'listingTitle': listing.listingTitle, 
                'description': listing.description,
                'currentBid': listing.currentBid,
                'category': listing.category
        }
           #     print("get method called")
        # form.fields['listingTitle'].initial = "TEST"
        # print("listingTitle:")
        # print(listing.listingTitle)
        # form.fields['description'].initial = listing.description
        
        # # form.fields['currentBid'].widget = forms.HiddenInput()
        # form.fields['category'].initial = listing.category
        form = AddListingForm(initial=data, instance=listing)
        form.fields['currentBid'].disabled = True
        return render(request, "auctions/edit_listing.html",{
            "form": form,
            "listing": listing
        })
    ### TEST END


    # if request.method == "GET":
    #     print("get method called")
    #     form.fields['listingTitle'].initial = listing.listingTitle
    #     form.fields['description'].initial = listing.description
    #     form.fields['currentBid'].initial = listing.currentBid
    #     # form.fields['currentBid'].widget = forms.HiddenInput()
    #     form.fields['category'].initial = listing.category
    #     ## TODO ## 
    #     # change listing image
    #     # form.fields['content'].initial = content
    #     return render(request, "auctions/edit_listing.html", {
    #         "form": form,
    #         "listing": listing
    #     })
    # # else:
    #     ## Method is post
    # if request.method == "POST":
    #     print("Post Method called")
    #     if form.is_valid():
    #         print("Post Method called and form is valid")
    #         listing = form.save()
    #         listing.save()
    #         print("Category Text")
    #         print(listing.category.categoryText)
    #         return HttpResponseRedirect(reverse("view_listing", args=(listing.id,)))
    
    #     print("HEREERERE")

    # return render(request, "auctions/edit_listing.html", {
    #     "form": form,
    #     "listing": listing
    # })