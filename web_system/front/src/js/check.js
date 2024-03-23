var IMAGE_URL = '';

function Check() {

}

Check.prototype.listenUploadFileEvent = function () {
    var uploadBtn = $('#upload-btn');
    uploadBtn.change(function () {
        // uploadBtn[0]：找到第一个uploadBtn标签
        // files[0]：files表示可以上传多个文件，在这里只要第一个文件
        var file = uploadBtn[0].files[0];
        var formData = new FormData();
        formData.append('file', file);
        $.ajax({
            'type': 'POST',
            'url': '/upload_img/',
            'data': formData,
            // 告诉jQuery不需要对文件格式进行处理了
            'processData': false,
            // 使用默认的文件形式，不需要在添加了
            'contentType': false,
            'success': function (result) {
                if (result['code'] === 200) {
                    IMAGE_URL = result['data']['url'];
                    var img_url = result['data']['url'];
                    var imageInput = $('#img-url');
                    imageInput.val(img_url);
                    var inputImg = $('.input-image-file');
                    inputImg.attr('src', img_url)
                }
            }
        })
    })
};


Check.prototype.listenImgCheckEvent = function () {
    var changeBtn = $('#img-change');
    changeBtn.click(function (event) {
        event.preventDefault();
        $.ajax({
            'type': 'POST',
            'url': '/check_img/',
            'data': {
                'img_url': IMAGE_URL,
            },
            'success': function (result) {
                if (result['code'] === 200) {
                    var pred_name = result['data']['pred_name'];
                    var info = result['data']['info'];
                    myalert.alertInfoWithTitle(pred_name, info);
                } else {
                    myalert.alertInfoWithTitle(result['message'], '错误信息')
                }
            }
        })
    })
}


Check.prototype.run = function () {
    var self = this;
    self.listenUploadFileEvent();
    self.listenImgCheckEvent();
};


$(function () {
    var check = new Check();
    check.run()
});


