class object_repository:

    #object
    page        = '//li[@ng-class="{completed: buyingReq.page > 1, active: buyingReq.page == 1}"]'
    form        = '//div[@class="rfq-form-text"]'
    subheader   = '//div[@class="rfq-subheader"]'

    #field
    name    = '//input[@name="name"]'
    email   = '//input[@name="email"]'
    country = '//select[@class="form-control ng-pristine ng-valid ng-not-empty ng-valid-required ng-touched" and @ng-model="form.country_code"]'
    phone   = '//input[@name="phone"]'

    #button
    nextbtn = '//button[@type="button" and @class="btn btn-primary btn-rfq-form pull-right"]'

    #message
    name_required   = '//div[@ng-show="buyingReq.accountInfo.name.$error.required"]'
    name_minlength  = '//div[@ng-show="buyingReq.accountInfo.name.$error.minlength"]'

    email_required  = '//div[@ng-show="buyingReq.accountInfo.email.$error.required"]'
    email_format    = '//div[@ng-show="buyingReq.accountInfo.email.$error.email"]'

    phone_validity  = '//div[@ng-show="buyingReq.accountInfo.phone.$error.validity"]'
    phone_required  = '//div[@ng-show="buyingReq.accountInfo.phone.$error.required"]'
    phone_minlength = '//div[@ng-show="buyingReq.accountInfo.phone.$error.minlength"]'

    errormessage    = '//div[contains(@ng-show="buyingReq.accountInfo.")]'
