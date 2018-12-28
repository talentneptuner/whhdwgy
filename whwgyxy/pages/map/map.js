// pages/map/map.js
var is_tablet
Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgurl:'http://www.whfles.com/UploadFiles/SingleNode/201803260908495653.jpg',
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    var sysinfo = wx.getSystemInfoSync();
    console.log(sysinfo);
    var scr_width = sysinfo.windowWidth;
    var scr_height = sysinfo.windowHeight;
    if (scr_width > 700 && scr_height > 900){
      is_tablet = true;
    }
    else{
      is_tablet = false
    }

    var that = this;
    wx.request({
      url: 'http://39.108.253.48/getsights/',
      method: 'GET',
      header: {
        'Accept': 'application/json'
      },
      success: function (res) {
        that.setData({
          sightlist: res.data,
        })
      }
    })
  
  },

  show : function(res){
    var name = res.currentTarget.dataset.name;
    var id = res.currentTarget.dataset.id;
    console.log(id);
    wx.showModal({
      title: name,
      content: '点击\n查看详情\n可以查看地点介绍与图片哦！',
      confirmText:'查看详情',
      cancelText:'回到地图',
      success:function(res){
        if(res.confirm){
         wx.navigateTo({
           url: '/pages/sightdetail/sightdetail?id='+id,
         })
        }
      }
    })
  },
  ToVR: function() {
    wx.setClipboardData({
      data: 'https://720yun.com/t/8554wedgawseg5oqc4?pano_id=FvkBhRqJpUOMU3bT',
      success: function(res){
        wx.showToast({
          title: '链接已复制',
        })
      }
    })
  },

  imgLoad: function(img){
    var w = img.detail.width;
    var h = img.detail.height;
    var width_cut = 0;
    var height_cut = 0;
    if (is_tablet){
      width_cut = 30;
      height_cut = 60;
    }
    else{
      width_cut = 30;
      height_cut = 40;
    }
    this.setData({
      image_width: w / 2,
      image_height: h / 2,
      scr_width: w / 2,
      scr_height: h / 2,
      width_cut : width_cut,
      height_cut : height_cut,
    });
    
  }

  
})