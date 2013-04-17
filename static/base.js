function Movie(name) {
    var self = this;
    self.name = name;
}



function ActivitiesViewModel(activities){
    var self = this;
    self.activities = ko.observableArray(ko.utils.arrayMap(activities, function(item) {
        return new ActivityModel(item);
    }));
    self.current_user = activities.current_user;
    self.deleteActivity = function(activity){
        $.ajax({
            url: '/ajax/delete/',
            type: 'POST',
            data: {
                id: activity.id
            },

            success: function(message){
                console.log('Success deleting the activity');
                self.activities.remove(activity);
            },
            error: function(message){
                console.error('Failed deleting the activity');
            }

        });
    };
}

function ActivityModel(activity){
    var self = this;

    for(var k in activity)
        self[k]=activity[k];
    self.act_text = {1:'owned', 2:'watched', 3:'liked', 4:'disliked', 5:'favorited', 6:'checked-in to'}[self.act];
    self.movie.full_title = self.movie.title+' ('+self.movie.year+')';
}


function ProfileModel(profile){
    var self = this;
    self.id = profile.user.id;
    self.username = profile.user.username;
    if (profile.current_user)
        self.current_user = profile.current_user;
    if (profile.following){

        self.followers = ko.utils.arrayMap(profile.followers, function(profile) {
            return new ProfileModel(profile);
        });

        self.following = ko.utils.arrayMap(profile.following, function(profile) {
            return new ProfileModel(profile);
        });

        self.is_followed = ko.computed(function() {
            for (var j in self.followers){
                if (self.current_user.username == self.followers[j].username)
                    return true;
            }
            return false;
        });

        self.follows = ko.computed(function() {
            for (var k in self.following){
                if (self.current_user.username == self.following[k].username)
                    return true;
            }
            return false;
        });

        self.relation = ko.computed(function() {
            if (self.current_user.username == self.username)
                return 'self';
            if (self.is_followed() && self.follows()) return 'mutual';
            if (self.is_followed()) return 'is_followed';
            if (self.follows()) return 'follows';
            return 'oblivious';
        });
    }
}

function MovieModel(movie){
    var self = this;
    for(var k in movie)
        self[k]=movie[k];
    self.directors = ko.utils.arrayMap(movie.directors, function(director) {
        return new DirectorModel(director);
    });
    self.directors_name = ko.computed(function(){
        str = '';
        for (var i=0; i<self.directors.length; i++){
            if (i) str+= ', ';
            str += self.directors[i].name;
        }
        return str;
    });
    self.full_title = self.title+' ('+self.year+')';

    if (!self.user_data) self.user_data = [];
    //convert all toggle keys to observables
    user_data = ['watched', 'owned', 'liked', 'disliked', 'favorited'];
    for (var key in user_data){
        if (movie.user_data)
            self[user_data[key]] = ko.observable(movie.user_data[user_data[key]]);
        else
            self[user_data[key]] = ko.observable(false);
    }
    self.docheckin = function(data, el){
        el.target.innerHTML = 'Checking in ...';
        $.ajax({
            url: '/ajax/movie/checkin/',
            type: 'POST',
            data: {
                id: self.id
            },

            success: function(message){
                    // upon successful checkin, set watched to true
                    self.watched(true);
                    el.target.innerHTML = 'Checked in!';
                    $(el.target).off('click');
                },
                error: function(message){
                    el.target.innerHTML = 'Checked in failed!';
                    alert(message);
                }

            });
    };
}

function DirectorModel(director){
    var self = this;
    for(var k in director) self[k]=director[k];
}

function ListViewModel(data, list_container) {
    if (typeof list_container == 'undefined')
        list_container = 'items';
    var self = this;
    for(var k in data)
        self[k]=data[k];
    self[list_container] = ko.utils.arrayMap(data[list_container], function(item) {
        return new MovieModel(item);
    });
    if (self[list_container].length===0){
        $('#list-container').html('No movies found!');
    }
}

function ListListModel(data) {
    var self = this;
    for(var k in data)
        self[k]=data[k];
    self['items'] = ko.utils.arrayMap(data['items'], function(item) {
        return new ListItemModel(item);
    });
    if (self.items.length===0){
        $('#list-container').html('No lists found!');
    }
}

function ListItemModel(data){
    var self = this;
    for(var k in data)
        self[k]=data[k];
    self['on_watchlist'] = ko.observable(data['user_data']['on_watchlist']);
    self['favorited'] = ko.observable(data['user_data']['favorited']);
}

function MovieViewModel(data) {
    var self = this;
    for(var k in data)
        self[k]=data[k];
    // self.items = ko.utils.arrayMap(data.items, function(item) {
    //     return new MovieModel(item);
    // });

}

ko.bindingHandlers.relative = {
    update: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        var valueUnwrapped = ko.utils.unwrapObservable(valueAccessor());
        element.innerHTML = moment(valueUnwrapped).fromNow();
    }
};

ko.bindingHandlers.toggle = {
    init: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        $(element).change(function() {
            //onchange of checkbox update observable
            var value = valueAccessor();
            value(element.checked);
            model_name = viewModel.constructor.name.replace('Model','').toLowerCase();
            className = element.className;
            $(element).addClass('loading');
            $.ajax({
                url: '/ajax/'+model_name+'/',
                type: 'POST',
                data: {
                    id: viewModel.id,
                    attr: className,
                    value: element.checked
                },

                success: function(message){
                    $(element).removeClass('loading');

                },
                error: function(message){
                    $(element).removeClass('loading');
                    //toggle back the checkbox
                    $(element).prop('checked', !$(element).prop('checked'));
                    alert(message);
                }

            });
        });
    },
    update: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        //on update of observable change checkbox
        var valueUnwrapped = ko.utils.unwrapObservable(valueAccessor());
        element.checked = valueUnwrapped;
    }
};

ko.bindingHandlers.follow = {
    init: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {

        $(element).hover(
            function(){
                var hover_text = '';
                if (viewModel.relation() == 'self')
                    return;
                if (viewModel.is_followed())
                    hover_text = 'Unfollow!';
                else
                    hover_text = 'Follow!';
                $(element).html(hover_text);
            },
            function(){
                $(element).html(text[viewModel.relation()]);
            }
            );

        $(element).click(function() {
            $(element).html('...');
            if (viewModel.relation() == 'self') return;
            action = (viewModel.is_followed())? 'unfollow' : 'follow';
            $.ajax({
                url: '/ajax/'+action+'/',
                type: 'POST',
                data: {
                    user: viewModel.username
                },

                success: function(message){
                    if (action=='follow'){
                        $(element).html('Followed!');
                        $(element).off('mouseenter mouseleave');
                        $(element).off('click');
                    }
                    if (action=='unfollow'){
                        $(element).html('Unfollowed!');
                        $(element).off('mouseenter mouseleave');
                        $(element).off('click');
                    }
                },
                error: function(message){
                    // $(element).removeClass('loading');
                    // //toggle back the checkbox
                    // $(element).prop('checked', !$(element).prop('checked'));
                    // alert(message);
                    console.log('unsuccess');
                }

            });
});
        //find relation between the logged in user and user of the profile


    },
    update: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        //on update of observable change checkbox
        // var valueUnwrapped = ko.utils.unwrapObservable(valueAccessor());
        // element.checked = valueUnwrapped;
        text = {'oblivious':'Follow!', 'self': 'That\'s you!', 'mutual': 'Following each other!', 'is_followed': 'You follow!', 'follows': 'Follows you!'};
        $(element).html(text[viewModel.relation()]);
    }
};
