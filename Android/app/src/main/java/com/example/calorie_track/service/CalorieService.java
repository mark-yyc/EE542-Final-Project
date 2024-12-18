package com.example.calorie_track.service;

import com.example.calorie_track.data.CalorieInfo;
import com.example.calorie_track.data.CommuteInfo;

import retrofit2.Call;
import retrofit2.http.GET;

public interface CalorieService {
    @GET("calorie_today")
    Call<CalorieInfo> getCalorieInfo();

    @GET("calorie_commute")
    Call<CommuteInfo> getCommuteInfo();

    @GET("upload_image")
    Call<CalorieInfo> uploadImage();
}
