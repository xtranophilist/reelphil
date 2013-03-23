function Movie(name) {
    var self = this;
    self.name = name;
}

function ProfileModel(profile){
    var self = this;
    self.id = profile.user.id;
    self.username = profile.user.username;
    if (profile.current_user)
        self.current_user = profile.current_user;
    if (profile.followers)
        self.followers = ko.utils.arrayMap(profile.followers, function(profile) {
            return new ProfileModel(profile);
        });
    if (profile.following)
        self.following = ko.utils.arrayMap(profile.following, function(profile) {
            return new ProfileModel(profile);
        });

    if (profile.following){
        self.relation = ko.computed(function() {
            if (self.current_user.username == self.username)
                return 'self';
            var is_followed = false;
            var followed_by = false;
            for (var j in self.followers){
                if (self.current_user.username == self.followers[j].username)
                    followed_by = true;
            }
            for (var k in self.following){
                if (self.current_user.username == self.following[k].username)
                    is_followed = true;
            }
            if (is_followed && followed_by) return 'mutual';
            if (is_followed) return 'following';
            if (followed_by) return 'follows';
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
    console.log(self);
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
}

function MovieViewModel(data) {
    var self = this;
    console.log(data);

    for(var k in data)
        self[k]=data[k];
    // self.items = ko.utils.arrayMap(data.items, function(item) {
    //     return new MovieModel(item);
    // });
    // console.log(self);

}

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
        text = {'oblivious':'Follow!', 'self': 'That\'s you!', 'mutual': 'Following each other!', 'following': 'You follow!', 'follows': 'Follows you!'};
        $(element).html(text[viewModel.relation()]);
        $(element).hover(
            function(){
                var hover_text = '';
                if (viewModel.relation() == 'self')
                    return;
                if (viewModel.relation() == 'mutual' || viewModel.relation() == 'following')
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
            console.log('hiya');

            // alert (1);
            // var value = valueAccessor();
            // value(element.checked);
            // model_name = viewModel.constructor.name.replace('Model','').toLowerCase();
            // className = element.className;
            // $(element).addClass('loading');
            // $.ajax({
            //     url: '/ajax/'+model_name+'/',
            //     type: 'POST',
            //     data: {
            //         id: viewModel.id,
            //         attr: className,
            //         value: element.checked
            //     },

            //     success: function(message){
            //         $(element).removeClass('loading');

            //     },
            //     error: function(message){
            //         $(element).removeClass('loading');
            //         //toggle back the checkbox
            //         $(element).prop('checked', !$(element).prop('checked'));
            //         alert(message);
            //     }

            // });
});
        //find relation between the logged in user and user of the profile


    },
    update: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        //on update of observable change checkbox
        // var valueUnwrapped = ko.utils.unwrapObservable(valueAccessor());
        // element.checked = valueUnwrapped;
    }
};
