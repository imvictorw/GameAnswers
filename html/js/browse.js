$(document).ready(function () {

    $.fn.disableTab = function (tabIndex, hide) {

        var disabledTabs = this.tabs("option", "disabled");

        if ($.isArray(disabledTabs)) {
            var pos = $.inArray(tabIndex, disabledTabs);
            if (pos < 0)
                disabledTabs.push(tabIndex);
        }
        else
            disabledTabs = [tabIndex];

        this.tabs("option", "disabled", disabledTabs);

        if (hide === true)
            $(this).find('li:eq(' + tabIndex + ')').addClass('ui-state-hidden');

        return this;
    };

    $.fn.enableTab = function (tabIndex) {
        $(this).find('li:eq(' + tabIndex + ')').removeClass('ui-state-hidden');
        this.tabs("enable", tabIndex);
        return this;
    };

    $("#tabs").tabs();

});
