'use strict';

/* https://github.com/angular/protractor/blob/master/docs/toc.md */

describe('my app', function() {


  it('should automatically redirect to / when location hash/fragment is empty', function() {
    browser.get('/');
    expect(browser.getLocationAbsUrl()).toMatch("/");
  });


  describe('twitter-view', function() {

    beforeEach(function() {
      browser.get('/');
    });


    it('should render twitter-view when user navigates to /', function() {
      expect(element.all(by.css('[ng-view] p')).first().getText()).
        toMatch('/static/twitter/angular-seed/app/twitter-view/twitter-view.html');
    });

  });
});
