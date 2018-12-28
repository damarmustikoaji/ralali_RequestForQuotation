class object_repository:

    #object
    page        = '//li[@ng-class="{completed: buyingReq.page > 2, active: buyingReq.page == 2}"]'
    form        = '//div[@class="rfq-form-text"]'
    subheader   = '//div[@class="rfq-subheader"]'

    #field
    item_service    = '//input[@name="item_service" and @placeholder="need plastic packaging"]'
    suggestion      = '//ul[@class="dropdown-menu" and @role="listbox"]'
    category        = '//input[@class="form-control ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required" and @placeholder="Select Category"]'
    categoryselector= '//div[@class="category-selector"]'
    categorybtn     = '//button[@class="btn btn-sm btn-primary hidden-xs" and @ng-click="doSelectCategory()"]'
    description     = '//textarea[@name="description"]'
    quantity        = '//input[@name="quantity"]'
    unit            = '//select[@name="unit"]'

    #additional form
    add             = '//div[@ng-click="buyingReq.openRequirement = true;"]/div[@class="item-align-center requirement-wrapper"]'

    #button
    findmebtn       = '//button[@class="btn btn-primary btn-rfq-form pull-right" and @ng-click="buyingReq.saveDetailInfo(1)"]'
    backbtn         = '//a[@ng-click="buyingReq.page = 1" and @class="btn-rfq-back"]'

    #message
    item_required   = '//div[@ng-show="buyingReq.detailInfo.item_service.$error.required"]'
    item_minlength  = '//div[@ng-show="buyingReq.detailInfo.item_service.$error.minlength"]'

    desc_required   = '//div[@ng-show="buyingReq.detailInfo.description.$error.required"]'
    desc_minlength  = '//div[@ng-show="buyingReq.detailInfo.description.$error.minlength"]'

    qt_minlength    = '//div[@ng-show="(buyingReq.detailInfo.quantity.$touched || buyingReq.detailInfo.$submitted )&& buyingReq.detailInfo.quantity.$invalid"]'
    qt_error        = '//*[contains(text(), "Quantity cannot be blank and must be digits")]'

    errormessage    = '//div[contains(@ng-show="buyingReq.accountInfo.")]'
