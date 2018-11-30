$(function (row) {
    //给全选的复选框添加事件
    $("#all").click(function () {
        // this 全选的复选框
        var userids = this.checked;
        //获取name=box的复选框 遍历输出复选框
        $("input[name=box]").each(function () {
            this.checked = userids;
        });
    });
    //给name=box的复选框绑定单击事件
    //获取选中复选框长度
    //未选中的长度
    //给全选的复选框添加事件
    $("#all1").click(function () {
        // this 全选的复选框
        var userids = this.checked;
        //获取name=box的复选框 遍历输出复选框
        $("input[name=box]").each(function () {
            this.checked = userids;
        });
    });

    $("input[name=box]").click(function () {
        var length = $("input[name=box]:checked").length;
        var len = $("input[name=box]").length;
        if (length == len) {
            $("#all").get(0).checked = true;
        } else {
            $("#all").get(0).checked = false;
        }
    });
    $(".add").click(function () {
        var n = $(this).prev().val();
        var num = parseInt(n) + 1;
        if (num == 0) {
            return;
        }
        $(this).prev().val(num);
    });
//减的效果
    $(".jian").click(function () {
        var n = $(this).next().val();
        var num = parseInt(n) - 1;
        if (num == 0) {
            return
        }
        $(this).next().val(num);
    });


});

