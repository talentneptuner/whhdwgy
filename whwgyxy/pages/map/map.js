// pages/map/map.js
var scr_width
var scr_height

Page({

  /**
   * 页面的初始数据
   */
  data: {
    imgurl:'http://www.whfles.com/UploadFiles/SingleNode/201803260908495653.jpg',
    imageheight : 1240 ,
    imagewidth : 1683 ,
  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

    var sysinfo = wx.getSystemInfoSync();
    console.log(sysinfo);
    scr_width = sysinfo.screenWidth;
    scr_height = sysinfo.screenHeight;
    this.setData({
      w : scr_width,
      h : scr_height,
    });
    console.log(scr_width);

    var that = this;
    wx.request({
      url: 'http://localhost:8000/getsights/',
      method: 'GET',
      header: {
        'Accept': 'application/json'
      },
      success: function (res) {
        console.log(res.data);
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
  }

  
})