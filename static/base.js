function Movie(name) {
    var self = this;
    self.name = name;
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
    if (movie.user_data){
        self.watched = ko.observable(movie.user_data.watched);
        self.owned = ko.observable(movie.user_data.owned);
    }else{
        self.watched = false;
        self.owned = false;
    }
}

function DirectorModel(director){
    var self = this;
    for(var k in director) self[k]=director[k];
}

function ListViewModel(data) {
    var self = this;
    for(var k in data)
        self[k]=data[k];
    self.items = ko.utils.arrayMap(data.items, function(item) {
        return new MovieModel(item);
    });
    console.log(self);

}

ko.bindingHandlers.toggle = {
    init: function(element, valueAccessor, allBindingsAccessor, viewModel, bindingContext) {
        $(element).change(function() {
            //onchange of checkbox update observable
            console.log(valueAccessor());
            var value = valueAccessor();
            value(element.checked);
            $.ajax({
                url: '/movie/',
                type: 'POST',
                data: {
                    id: viewModel.id,
                    attr: element.className,
                    value: element.checked
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


