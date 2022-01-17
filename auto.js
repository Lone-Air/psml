$(function(){
    $.fn.autoHeight = function(){
        function autoHeight(elem){
            elem.style.height = 'auto';
            elem.scrollTop = 0;
            elem.style.height = (elem.scrollHeight)+2 + 'px';
        }
        this.each(function(){
            autoHeight(this);
            $(this).on('input', function(){
                autoHeight(this);
            });
        });
    }
    $('textarea[autoHeight]').autoHeight();
})

$("textarea").on(
            'keydown',
            function(e) {
                if (e.keyCode == 9) {
                    e.preventDefault();
                    var indent = '    ';
                    var start = this.selectionStart;
                    var end = this.selectionEnd;
                    var selected = window.getSelection().toString();
                    selected = indent + selected.replace(/\n/g, '\n' + indent);
                    this.value = this.value.substring(0, start) + selected + this.value.substring(end);
                    this.setSelectionRange(start + indent.length, start + selected.length);
                }
            })
