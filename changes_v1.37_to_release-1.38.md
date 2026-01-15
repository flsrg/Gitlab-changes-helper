# GitLab changes: v1.37 → release-1.38

- Project: `jackes/calendar`
- GitLab: https://gitlab.com
- Compare page: https://gitlab.com/jackes/calendar/-/compare/1abc70d1455df7b9678962ac014825d39b198bda..1a7f60fdfb1010932b1b78dd06e4678772aa61c6

## Summary

- Commits in range: **17**

### Files changed (from compare)

- `.gitlab-ci.yml`
- `android-utils`
- `app/build.gradle`
- `app/src/main/java/com/itbenefit/android/calendar/ui/FAQActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/LicenseInfoActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/TutorialActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/WelcomeActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/settings/SettingsActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/utils/SupportEmailHelper.kt`
- `app/src/main/res/drawable-v31/bg_def.xml` (new)
- `app/src/main/res/values-ru/strings.xml`
- `app/src/main/res/values-v35/styles.xml` (new)
- `app/src/main/res/values/strings.xml`
- `app/src/main/res/values/styles.xml`
- `build.gradle`
- `gradle/wrapper/gradle-wrapper.properties`
- `key/build.gradle`

## Merge request !55 Removed signingConfig argument for release build

- MR URL: https://gitlab.com/jackes/calendar/-/merge_requests/55
- State: merged
- Merged at: 2024-10-02T06:55:47.665Z
- Author: Maxim Shcherbakov
- Branches: `remove-signing-config-arg` → `master`

**Description:**

```text
Was added accidentally. Removed.

Tests Android 14:
- Build and run.
```

### Commits (detailed)

#### 1. `74a054e3` Removed signingConfig argument for release build

- SHA: `74a054e3ed73079edfca9269bef0ce73855a5344`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/74a054e3ed73079edfca9269bef0ce73855a5344
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2024-09-27T16:38:53.000+07:00

**Full commit message:**

```text
Removed signingConfig argument for release build

Was added accidentally. Removed.

Tests Android 14:
- Build and run.
```

**Diff (per commit):**

##### `app/build.gradle`

```diff
--- a/app/build.gradle
+++ b/app/build.gradle
@@ -26,7 +26,6 @@ android {
             shrinkResources true
             proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
             buildConfigField "boolean", BUILD_CONFIG_LOG, "false"
-            signingConfig signingConfigs.debug
         }
     }
```

**Files touched in this MR (derived from commit diffs):**
- `app/build.gradle`

---

## Merge request !56 Merge release-1.37 into master

- MR URL: https://gitlab.com/jackes/calendar/-/merge_requests/56
- State: merged
- Merged at: 2024-10-11T03:02:03.534Z
- Author: Evgeny Braychuk
- Branches: `release-1.37` → `master`

**Description:**

```text
Version 1.37 (widget app) and 1.3 (key app) published on Google Play
```

### Commits (detailed)

#### 1. `dd0bec86` [key-app] Bump version to 1.3 (4)

- SHA: `dd0bec86d56a06db72c636f99eb0bf76754b2978`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/dd0bec86d56a06db72c636f99eb0bf76754b2978
- Author: Evgeny Braychuk <braychuken@gmail.com>
- Created: 2024-10-10T08:56:43.000+00:00

**Full commit message:**

```text
[key-app] Bump version to 1.3 (4)
```

**Diff (per commit):**

##### `key/build.gradle`

```diff
--- a/key/build.gradle
+++ b/key/build.gradle
@@ -9,8 +9,8 @@ android {
         targetSdkVersion 34
         compileSdk 34
         buildToolsVersion = '34.0.0'
-        versionCode 3
-        versionName "1.2"
+        versionCode 4
+        versionName "1.3"
         setProperty("archivesBaseName", "calendar_key-$versionName")
     }
```

#### 2. `4c328037` Bump version to 1.37 (55)

- SHA: `4c328037adb263761a2a84e4f86a3c4fa872e375`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/4c328037adb263761a2a84e4f86a3c4fa872e375
- Author: Evgeny Braychuk <braychuken@gmail.com>
- Created: 2024-10-10T08:56:43.000+00:00

**Full commit message:**

```text
Bump version to 1.37 (55)
```

**Diff (per commit):**

##### `app/build.gradle`

```diff
--- a/app/build.gradle
+++ b/app/build.gradle
@@ -12,8 +12,8 @@ android {
         targetSdkVersion 34
         compileSdk 34
         buildToolsVersion = "34.0.0"
-        versionCode 54
-        versionName "1.36"
+        versionCode 55
+        versionName "1.37"
         resConfigs "ru"
         setProperty("archivesBaseName", "calendar-$versionName")
         buildConfigField "boolean", BUILD_CONFIG_LOG, "true"
```

**Files touched in this MR (derived from commit diffs):**
- `app/build.gradle`
- `key/build.gradle`

---

## Merge request !58 Resolve #74 "Bump target API level to 35, update libs and tools"

- MR URL: https://gitlab.com/jackes/calendar/-/merge_requests/58
- State: merged
- Merged at: 2025-08-13T10:57:37.066Z
- Author: Maxim Shcherbakov
- Branches: `74-bump-target-sdk-libs-and-tools` → `master`

**Description:**

```text
### Changes

<details><summary>Android 15 (targetSDK 35)</summary>

[Android 15](https://developer.android.com/about/versions/15)

# All apps 
### Support for 16 KB page sizes
[link](https://developer.android.com/about/versions/15/behavior-changes-all#16-kb)
> If your app [uses any native code](https://developer.android.com/guide/practices/page-sizes#native-code), then you should [rebuild your app with support for 16 KB devices](https://developer.android.com/guide/practices/page-sizes#build). If you are unsure if your app uses native code, you can [use the APK Analyzer to identify whether any native code is present](https://developer.android.com/guide/practices/page-sizes#identify-native-code) and then [check the alignment of ELF segments for any shared libraries](https://developer.android.com/guide/practices/page-sizes#elf-alignment) that you find. Android Studio also provides features that help you to [automatically detect alignment issues](https://developer.android.com/guide/practices/page-sizes#auto-checks).

> If your app only uses code written in the Java programming language or in Kotlin, including all libraries or SDKs, then your app already supports 16 KB devices. Nevertheless, we recommend that you [test your app in a 16 KB environment](https://developer.android.com/guide/practices/page-sizes#test) to verify that there are no unexpected regressions in app behavior.
#### [[Calendar]]
- Doesn't use any native libs. Skip. 
	- *Tested in 16KB version of Android 15 on Pixel 9 emulator.*

### Required changes for some apps to support private space
[link](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-changes)
Android 15 adds Private Space (separate profile for sensitive apps). Apps must update work profile logic to handle multiple profile types, not just one.
#### [[Calendar]]
- I haven't found any launchers that support private space.
- Content Provider should work. Or throws an understandable exception if the fetching restricted.

### PNG-based emoji font removed
[link](https://developer.android.com/about/versions/15/behavior-changes-all#png-emoji-font)
> The legacy, PNG-based emoji font file (`NotoColorEmojiLegacy.ttf`) has been removed

#### Calendar
- Doesn't use. Skip.

### Predictive back animations enabled for apps that opted in
[link](https://developer.android.com/about/versions/15/behavior-changes-all#predictive-back)
> Beginning in Android 15, the developer option for [predictive back animations](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture) has been removed. System animations such as back-to-home, cross-task, and cross-activity now appear for apps that have [opted in to the predictive back gesture](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#opt-predictive) either entirely or at an activity level. If your app is affected, take the following actions:

- Ensure that your app has been properly migrated to use the predictive back gesture.
- Ensure that your fragment transitions work with predictive back navigation.
- Migrate away from animation and framework transitions and use animator and androidx transitions instead.
- Migrate away from back stacks that `FragmentManager` doesn't know about. Use back stacks managed by `FragmentManager` or by the Navigation component instead.

#### [[Calendar]]
- Doesn't supported, so doesn't work.

### Widgets disabled when user force-stops an app
[link](https://developer.android.com/about/versions/15/behavior-changes-all#widgets-force-stop)
> If a user force-stops an app on a device running Android 15, the system temporarily disables all the app's widgets. The widgets are grayed out, and the user cannot interact with them.

> [!TIP] 
> The system re-enables those widgets the next time the user launches the app.

#### [[Calendar]]
- It starts normally after force stop. Ok.

### Background network access restrictions
[link](https://developer.android.com/about/versions/15/behavior-changes-all#background-network-access)
> In Android 15, apps that start a network request outside of a valid [process lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle) receive an exception. Typically, an [`UnknownHostException`](https://developer.android.com/reference/java/net/UnknownHostException) or other socket-related `IOException`. Network requests that happen outside of a valid lifecycle are usually due to apps unknowingly continuing a network request even after the app is no longer active.

#### [[Calendar]]
- Doesn't fetch anything outside the Lifecycle. Ok.

# Apps targeting Android 15
### Changes to foreground services
[link](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-hardening)

> We are making the following changes to foreground services with Android 15.

- [Data sync foreground service timeout behavior](https://developer.android.com/about/versions/15/behavior-changes-15#datasync-timeout)
- [New media processing foreground service type](https://developer.android.com/about/versions/15/behavior-changes-15#mediaprocessing-fgs-type)
- [Restrictions on `BOOT_COMPLETED` broadcast receivers launching foreground services](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-boot-completed)
- [Restrictions on starting foreground services while an app holds the `SYSTEM_ALERT_WINDOW` permission](https://developer.android.com/about/versions/15/behavior-changes-15#fgs-sysalert)

#### [[Calendar]]
- Doesn't use foreground services. Ok.

### OpenJDK API changes
[link](https://developer.android.com/about/versions/15/behavior-changes-15#openjdk-api-changes)
> **Changes to string formatting APIs**: Validation of argument index, flags, width, and precision are now more strict when using the following `String.format()` and `Formatter.format()` APIs:

> - [`String.format(String, Object[])`](https://developer.android.com/reference/java/lang/String#format\(java.lang.String,%20java.lang.Object%5B%5D\))
> - [`String.format(Locale, String, Object[])`](https://developer.android.com/reference/java/lang/String#format\(java.util.Locale,%20java.lang.String,%20java.lang.Object%5B%5D\))
> - [`Formatter.format(String, Object[])`](https://developer.android.com/reference/java/util/Formatter#format\(java.lang.String,%20java.lang.Object%5B%5D\))
> - [`Formatter.format(Locale, String, Object[])`](https://developer.android.com/reference/java/util/Formatter#format\(java.util.Locale,%20java.lang.String,%20java.lang.Object%5B%5D\))

> For example, the following exception is thrown when an argument index of 0 is used (`%0` in the format string):

- Calendar: ? 

> **Changes to component type of `Arrays.asList(...).toArray()`**: When using `Arrays.asList(...).toArray()`, the component type of the resulting array is now an [`Object`](https://developer.android.com/reference/java/lang/Object)—not the type of the underlying array's elements. So the following code throws a [`ClassCastException`](https://developer.android.com/reference/java/lang/ClassCastException):

- Calendar: **Ok.**

> The new [`SequencedCollection`](https://developer.android.com/reference/java/util/SequencedCollection) API can affect your app's compatibility after you [update `compileSdk` in your app's build configuration to use Android 15 (API level 35)](https://developer.android.com/about/versions/15/setup-sdk#config):

> - **Collision with [`MutableList.removeFirst()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/remove-first.html) and [`MutableList.removeLast()`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/remove-last.html) extension functions in `kotlin-stdlib`**
> If an app is re-compiled with `compileSdk` set to `35` and `minSdk` set to `34` or lower, and then the app is run on Android 14 and lower, a runtime error is thrown:

- Calendar: **Ok.**

### Safer intents
[link](https://developer.android.com/about/versions/15/behavior-changes-15#safer-intents)

> - **Match target intent-filters:** Intents that target specific components must accurately match the target's intent-filter specifications. If you send an intent to launch another app's activity, the target intent component needs to align with the receiving activity's declared intent-filters.
> - **Intents must have actions:** Intents without an action will no longer match any intent-filters. This means that intents used to start activities or services must have a clearly defined action.

> In order to check how your app responds to these changes, use [`StrictMode`](https://developer.android.com/reference/android/os/StrictMode) in your app. To see detailed logs about `Intent` usage violations, add the following method:

```java
public void onCreate() {
    StrictMode.setVmPolicy(new VmPolicy.Builder()
            .detectUnsafeIntentLaunch()
            .build());
}
````

#### Calendar

1. Close [`SettingsActivity`](https://gitlab.com/jackes/calendar/blob/master/app/src/main/java/com/itbenefit/android/calendar/ui/settings/SettingsActivity.java#L167-167)

   * Error

   ```
   2025-08-02 15:07:46.273  4587-4587  WidgetActionReceiver    com.itbenefit.android.calendar       I  Intent { act=WidgetUpdater.ACTION_update flg=0x10 xflg=0x4 cmp=com.itbenefit.android.calendar/.widget.WidgetActionReceiver (has extras) }
                                                                                                       extras: action="update" caller="settings" settingsUpdated=true widgetIds=[9]
   2025-08-02 15:07:46.273  4587-4587  App                     com.itbenefit.android.calendar       I  Await background tasks (took 0 ms)
   2025-08-02 15:07:46.275  4587-5202  RemoteConfig            com.itbenefit.android.calendar       I  activation: nothing to activate
   2025-08-02 15:07:46.275  4587-5202  RemoteConfig            com.itbenefit.android.calendar       W  wait activate 2 ms
   2025-08-02 15:07:46.276  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       D  onHandleIntent: Intent { act=WidgetUpdater.ACTION_update flg=0x10 xflg=0x4 cmp=com.itbenefit.android.calendar/.widget.WidgetActionReceiver (has extras) }
                                                                                                       extras: action="update" caller="settings" settingsUpdated=true widgetIds=[9]
   2025-08-02 15:07:46.276  4587-5202  AppLog                  com.itbenefit.android.calendar       I  [updater] Intent { act=WidgetUpdater.ACTION_update flg=0x10 xflg=0x4 cmp=com.itbenefit.android.calendar/.widget.WidgetActionReceiver (has extras) }
                                                                                                       	extras: action="update" caller="settings" settingsUpdated=true widgetIds=[9]
   2025-08-02 15:07:46.279  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       D  Perform action: update, widgetId = 9, extras: action="update" caller="settings" settingsUpdated=true widgetIds=[9]
   2025-08-02 15:07:46.281  4587-5202  WidgetInstance          com.itbenefit.android.calendar       I  Read settings: widgetId = 9
   2025-08-02 15:07:46.286  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       I  Update widget (widgetId = 9)...
   2025-08-02 15:07:46.360  4587-5202  CalendarHelper          com.itbenefit.android.calendar       I  Query events: begin = 2025-07-29 00:00:00 +07; end = 2025-09-07 00:00:00 +07; excluded = null
   2025-08-02 15:07:46.370  4587-5202  CalendarHelper          com.itbenefit.android.calendar       I  Events fetched: 9
   2025-08-02 15:07:46.370  4587-5202  WidgetInstance          com.itbenefit.android.calendar       I  loadEvents (took 83 ms): begin=2025-07-29 00:00:00 +07, end=2025-09-07 00:00:00 +07, count=9
   2025-08-02 15:07:46.370  4587-5202  LayoutBuilder           com.itbenefit.android.calendar       I  Build widget layout (widgetId = 9)...
   2025-08-02 15:07:46.411  4587-5202  MarkDrawer              com.itbenefit.android.calendar       D  createBitmap: 0x80333333
   2025-08-02 15:07:46.412  4587-5202  MarkDrawer              com.itbenefit.android.calendar       D  createBitmap: 0x26333333
   2025-08-02 15:07:46.444  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:07:46.451  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:07:46.456  4587-5202  SaleConfig              com.itbenefit.android.calendar       D  Don't show sale: license valid
   2025-08-02 15:07:46.459  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:07:46.497  4587-5219  StrictMode              com.itbenefit.android.calendar       D  StrictMode policy violation: android.os.strictmode.UnsafeIntentLaunchViolation: Launch of unsafe intent: Intent { dat=intent: cmp=com.itbenefit.android.calendar/.widget.AgendaItemsService (has extras) } (Ask Gemini)
                                                                                                       	at android.os.StrictMode.onUnsafeIntentLaunch(StrictMode.java:2464)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13109)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13025)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13015)
                                                                                                       	at android.app.ContextImpl.bindServiceCommon(ContextImpl.java:2229)
                                                                                                       	at android.app.ContextImpl.bindService(ContextImpl.java:2114)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$ConnectionTask.<init>(AppWidgetManager.java:1690)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.lambda$connectAndConsumeInner$1(AppWidgetManager.java:1675)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.$r8$lambda$ZDcQMTsLKFfCK1gXzOZS0Db8mUU(Unknown Source:0)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$$ExternalSyntheticLambda0.apply(D8$$SyntheticClass:0)
                                                                                                       	at java.util.Map.computeIfAbsent(Map.java:1066)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.connectAndConsumeInner(AppWidgetManager.java:1674)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.lambda$connectAndConsume$0(AppWidgetManager.java:1669)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.$r8$lambda$v7HIrr9hPZryvu7LbHxJe-cE0YE(Unknown Source:0)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$$ExternalSyntheticLambda1.run(D8$$SyntheticClass:0)
                                                                                                       	at android.os.Handler.handleCallback(Handler.java:995)
                                                                                                       	at android.os.Handler.dispatchMessage(Handler.java:103)
                                                                                                       	at android.os.Looper.loopOnce(Looper.java:248)
                                                                                                       	at android.os.Looper.loop(Looper.java:338)
                                                                                                       	at android.os.HandlerThread.run(HandlerThread.java:85)

   ```
2. `AlarmManager` [auto update](https://gitlab.com/jackes/calendar/blob/master/app/src/main/java/com/itbenefit/android/calendar/widget/WidgetUpdater.java#L366-366)

   * Error

   ```
   2025-08-02 15:00:55.028  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       D  onHandleIntent: Intent { act=WidgetUpdater.ACTION_update flg=0x14 xflg=0x4 cmp=com.itbenefit.android.calendar/.widget.WidgetActionReceiver (has extras) }
                                                                                                       extras: action="update" caller="alarm" android.intent.extra.ALARM_COUNT=1
   2025-08-02 15:00:55.028  4587-5202  AppLog                  com.itbenefit.android.calendar       I  [updater] Intent { act=WidgetUpdater.ACTION_update flg=0x14 xflg=0x4 cmp=com.itbenefit.android.calendar/.widget.WidgetActionReceiver (has extras) }
                                                                                                       	extras: action="update" caller="alarm" android.intent.extra.ALARM_COUNT=1
   2025-08-02 15:00:55.030  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       D  Perform action: update, widgetId = 9, extras: action="update" caller="alarm" android.intent.extra.ALARM_COUNT=1
   2025-08-02 15:00:55.031  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       I  Update widget (widgetId = 9)...
   2025-08-02 15:00:55.100  4587-5202  CalendarHelper          com.itbenefit.android.calendar       I  Query events: begin = 2025-07-29 00:00:00 +07; end = 2025-09-07 00:00:00 +07; excluded = null
   2025-08-02 15:00:55.113  4587-5202  CalendarHelper          com.itbenefit.android.calendar       I  Events fetched: 9
   2025-08-02 15:00:55.113  4587-5202  WidgetInstance          com.itbenefit.android.calendar       I  loadEvents (took 82 ms): begin=2025-07-29 00:00:00 +07, end=2025-09-07 00:00:00 +07, count=9
   2025-08-02 15:00:55.113  4587-5202  LayoutBuilder           com.itbenefit.android.calendar       I  Build widget layout (widgetId = 9)...
   2025-08-02 15:00:55.121  4587-5202  MarkDrawer              com.itbenefit.android.calendar       D  createBitmap: 0x80333333
   2025-08-02 15:00:55.122  4587-5202  MarkDrawer              com.itbenefit.android.calendar       D  createBitmap: 0x26333333
   2025-08-02 15:00:55.142  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:00:55.144  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:00:55.145  4587-5202  SaleConfig              com.itbenefit.android.calendar       D  Don't show sale: license valid
   2025-08-02 15:00:55.146  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:00:55.174  4587-5219  StrictMode              com.itbenefit.android.calendar       D  StrictMode policy violation: android.os.strictmode.UnsafeIntentLaunchViolation: Launch of unsafe intent: Intent { dat=intent: cmp=com.itbenefit.android.calendar/.widget.AgendaItemsService (has extras) } (Ask Gemini)
                                                                                                       	at android.os.StrictMode.onUnsafeIntentLaunch(StrictMode.java:2464)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13109)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13025)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13015)
                                                                                                       	at android.app.ContextImpl.bindServiceCommon(ContextImpl.java:2229)
                                                                                                       	at android.app.ContextImpl.bindService(ContextImpl.java:2114)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$ConnectionTask.<init>(AppWidgetManager.java:1690)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.lambda$connectAndConsumeInner$1(AppWidgetManager.java:1675)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.$r8$lambda$ZDcQMTsLKFfCK1gXzOZS0Db8mUU(Unknown Source:0)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$$ExternalSyntheticLambda0.apply(D8$$SyntheticClass:0)
                                                                                                       	at java.util.Map.computeIfAbsent(Map.java:1066)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.connectAndConsumeInner(AppWidgetManager.java:1674)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.lambda$connectAndConsume$0(AppWidgetManager.java:1669)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.$r8$lambda$v7HIrr9hPZryvu7LbHxJe-cE0YE(Unknown Source:0)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$$ExternalSyntheticLambda1.run(D8$$SyntheticClass:0)
                                                                                                       	at android.os.Handler.handleCallback(Handler.java:995)
                                                                                                       	at android.os.Handler.dispatchMessage(Handler.java:103)
                                                                                                       	at android.os.Looper.loopOnce(Looper.java:248)
                                                                                                       	at android.os.Looper.loop(Looper.java:338)
                                                                                                       	at android.os.HandlerThread.run(HandlerThread.java:85)
   ```
3. WidgetArrows

   * Error

   ```
   2025-08-02 15:08:42.621  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       D  onHandleIntent: Intent { act=WidgetUpdater.ACTION_curr_month flg=0x10000010 xflg=0x4 cmp=com.itbenefit.android.calendar/.widget.WidgetActionReceiver (has extras) }
                                                                                                       extras: action="curr_month" caller="widget" widgetIds=[9]
   2025-08-02 15:08:42.622  4587-5202  AppLog                  com.itbenefit.android.calendar       I  [updater] Intent { act=WidgetUpdater.ACTION_curr_month flg=0x10000010 xflg=0x4 cmp=com.itbenefit.android.calendar/.widget.WidgetActionReceiver (has extras) }
                                                                                                       	extras: action="curr_month" caller="widget" widgetIds=[9]
   2025-08-02 15:08:42.623  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       D  Perform action: curr_month, widgetId = 9, extras: action="curr_month" caller="widget" widgetIds=[9]
   2025-08-02 15:08:42.623  4587-5202  FirebaseTracker         com.itbenefit.android.calendar       I  Event: widget_interaction, action="curr_month" widget_layout="MONTH_AGENDA" (disabled)
   2025-08-02 15:08:42.624  4587-5202  WidgetInstance          com.itbenefit.android.calendar       I  Set active month: Month {year = 2025, month = 7}
   2025-08-02 15:08:42.624  4587-5202  WidgetUpdater           com.itbenefit.android.calendar       I  Update widget (widgetId = 9)...
   2025-08-02 15:08:42.641  4587-5202  CalendarHelper          com.itbenefit.android.calendar       I  Query events: begin = 2025-07-29 00:00:00 +07; end = 2025-09-07 00:00:00 +07; excluded = null
   2025-08-02 15:08:42.646  4587-5202  CalendarHelper          com.itbenefit.android.calendar       I  Events fetched: 9
   2025-08-02 15:08:42.646  4587-5202  WidgetInstance          com.itbenefit.android.calendar       I  loadEvents (took 22 ms): begin=2025-07-29 00:00:00 +07, end=2025-09-07 00:00:00 +07, count=9
   2025-08-02 15:08:42.646  4587-5202  LayoutBuilder           com.itbenefit.android.calendar       I  Build widget layout (widgetId = 9)...
   2025-08-02 15:08:42.649  4587-5202  MarkDrawer              com.itbenefit.android.calendar       D  createBitmap: 0x80333333
   2025-08-02 15:08:42.649  4587-5202  MarkDrawer              com.itbenefit.android.calendar       D  createBitmap: 0x26333333
   2025-08-02 15:08:42.665  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:08:42.666  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:08:42.668  4587-5202  SaleConfig              com.itbenefit.android.calendar       D  Don't show sale: license valid
   2025-08-02 15:08:42.668  4587-5202  HWUI                    com.itbenefit.android.calendar       W  Image decoding logging dropped!
   2025-08-02 15:08:42.680  4587-5219  StrictMode              com.itbenefit.android.calendar       D  StrictMode policy violation: android.os.strictmode.UnsafeIntentLaunchViolation: Launch of unsafe intent: Intent { dat=intent: cmp=com.itbenefit.android.calendar/.widget.AgendaItemsService (has extras) } (Ask Gemini)
                                                                                                       	at android.os.StrictMode.onUnsafeIntentLaunch(StrictMode.java:2464)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13109)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13025)
                                                                                                       	at android.content.Intent.prepareToLeaveProcess(Intent.java:13015)
                                                                                                       	at android.app.ContextImpl.bindServiceCommon(ContextImpl.java:2229)
                                                                                                       	at android.app.ContextImpl.bindService(ContextImpl.java:2114)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$ConnectionTask.<init>(AppWidgetManager.java:1690)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.lambda$connectAndConsumeInner$1(AppWidgetManager.java:1675)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.$r8$lambda$ZDcQMTsLKFfCK1gXzOZS0Db8mUU(Unknown Source:0)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$$ExternalSyntheticLambda0.apply(D8$$SyntheticClass:0)
                                                                                                       	at java.util.Map.computeIfAbsent(Map.java:1066)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.connectAndConsumeInner(AppWidgetManager.java:1674)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.lambda$connectAndConsume$0(AppWidgetManager.java:1669)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache.$r8$lambda$v7HIrr9hPZryvu7LbHxJe-cE0YE(Unknown Source:0)
                                                                                                       	at android.appwidget.AppWidgetManager$ServiceCollectionCache$$ExternalSyntheticLambda1.run(D8$$SyntheticClass:0)
                                                                                                       	at android.os.Handler.handleCallback(Handler.java:995)
                                                                                                       	at android.os.Handler.dispatchMessage(Handler.java:103)
                                                                                                       	at android.os.Looper.loopOnce(Looper.java:248)
                                                                                                       	at android.os.Looper.loop(Looper.java:338)
                                                                                                       	at android.os.HandlerThread.run(HandlerThread.java:85)
   ```

### User experience and system UI

[link](https://developer.android.com/about/versions/15/behavior-changes-15#ux)

#### Edge-to-edge enforcement

> Apps are edge-to-edge by default on devices running Android 15 if the app is targeting Android 15 (API level 35).

#### \[\[Calendar]]

* Breaks the navbar and status bar in all Activities.

#### Stable configuration

> If your app targets Android 15 (API level 35) or higher, `Configuration` no longer excludes the system bars. If you use the screen size in the `Configuration` class for layout calculation, you should replace it with better alternatives like an appropriate `ViewGroup`, `WindowInsets`, or `WindowMetricsCalculator` depending on your need.

#### \[\[Calendar]]

* Not used. Ok.

#### elegantTextHeight attribute defaults to true

> For apps targeting Android 15 (API level 35), the [`elegantTextHeight`](https://developer.android.com/reference/android/R.attr#elegantTextHeight) [`TextView`](https://developer.android.com/reference/android/widget/TextView) attribute becomes `true` by default, replacing the compact font used by default with some scripts that have large vertical metrics with one that is much more readable.

> So, if your app supports the following scripts: Arabic, Lao, Myanmar, Tamil, Gujarati, Kannada, Malayalam, Odia, Telugu or Thai, test your app by setting `elegantTextHeight` to `true`.

#### \[\[Calendar]]

* Doesn't support. Ok.

#### TextView width changes for complex letter shapes

> In previous versions of Android, some cursive fonts or languages that have complex shaping might draw the letters in the previous or next character's area. In some cases, such letters were clipped at the beginning or ending position. Starting in Android 15, a `TextView` allocates width for drawing enough space for such letters and allows apps to request extra paddings to the left to prevent clipping.

#### \[\[Calendar]]

* Not used. Ok.

#### Locale-aware default line height for EditText

> For apps targeting Android 15 (API level 35), a minimum line height is now reserved for `EditText` to match the reference font for the specified Locale, as shown in the following image:

![](https://developer.android.com/static/about/versions/15/images/locale-aware-line-height-after.png)

*Three boxes representing `EditText` elements that can contain text from English (en), Japanese (ja), and Burmese (my). The height of the `EditText` now includes space to accommodate the default line height for these languages' fonts.*

> If needed, your app can restore the previous behavior by specifying the [`useLocalePreferredLineHeightForMinimum`](https://developer.android.com/reference/android/R.attr#useLocalePreferredLineHeightForMinimum) attribute to `false`, and your app can set custom minimum vertical metrics using the [`setMinimumFontMetrics`](https://developer.android.com/reference/android/text/DynamicLayout.Builder#setMinimumFontMetrics%28android.graphics.Paint.FontMetrics%29) API in Kotlin and Java.

#### \[\[Calendar]]

* Ok.

</details>

---

<details><summary>Kotlin</summary>

### Kotlin 1.8
[link](https://kotlinlang.org/docs/whatsnew18.html)
#### Updated JVM compilation target
[link](https://kotlinlang.org/docs/whatsnew18.html?utm_source=chatgpt.com#updated-jvm-compilation-target)
> If you have explicitly declared `kotlin-stdlib-jdk7` and `kotlin-stdlib-jdk8` as dependencies in your build scripts, then you should replace them with `kotlin-stdlib`.

### Kotlin 2.2.0
[JetBrains official release notes](https://blog.jetbrains.com/kotlin/2025/06/kotlin-2-2-0-released/) | [What's new](https://kotlinlang.org/docs/whatsnew22.html)
Skip

</details>

---

<details><summary>AndroidX Core-ktx</summary>

## Core and Core-ktx Version 1.15.0 ([link](https://developer.android.com/jetpack/androidx/releases/core#1.15.0))
- Various updates to compatibility classes for parity with Android 15 SDK.
- requires sdk 35

## Core and Core-ktx Version 1.16 ([link](https://developer.android.com/jetpack/androidx/releases/core#core_and_core-ktx_version_116_2))
> This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Iaf3e1](https://android-review.googlesource.com/#/q/Iaf3e1d955e754d15c6b69b9fb397aad4b54aaf96), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Skip

</details>

---

<details><summary>AppCompat</summary>

## [1.7.1](https://developer.android.com/jetpack/androidx/releases/appcompat#1.7.1)
> `AppCompat` has been updated to use Activity 1.8.0 to allow it to use the `initializeViewTreeOwners()` API from `ComponentActivity` to ensure that it always has the correct `ViewTreeOwners` set. This fixes an incompatibility between `AppCompatActivity` and [NavigationEvent](https://developer.android.com/jetpack/androidx/releases/navigationevent) and libraries that build on top of it such as [Navigation 3](https://developer.android.com/jetpack/androidx/releases/navigation3). ([I96919](https://android-review.googlesource.com/#/q/I969192dacdbae2c6feb9734cafc21cd0ee352680), [b/419208471](https://issuetracker.google.com/issues/419208471))
- Skip

</details>

---

<details><summary>Firebase</summary>

**Use BoM to automatically resolve matching versions of firebase.**

### [Remote Config version 22.0.1](https://firebase.google.com/support/release-notes/android#remote-config_v22-0-1)
> - Updated protobuf dependency to `3.25.5` to fix [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254).
- Skip

### [Remote Config version 22.1.0](https://firebase.google.com/support/release-notes/android#remote-config_v22-1-0)
> - Added support for custom signal targeting in Remote Config. Use the [`setCustomSignals`](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfig#setCustomSignals\(com.google.firebase.remoteconfig.CustomSignals\)) API for setting custom signals to build custom targeting conditions in Remote Config.
- Skip

### [Remote Config version 22.1.1](https://firebase.google.com/support/release-notes/android#remote-config_v22-1-1)
> - Fixed an issue where the connection to the real-time Remote Config backend could remain open in the background.
- Skip

### [Remote Config version 22.1.2](https://firebase.google.com/support/release-notes/android#remote-config_v22-1-2)
> - Fixed `NetworkOnMainThreadException` on Android versions below 8 by disconnecting `HttpURLConnection` only on API levels 26 and higher. GitHub [#6941](https://github.com/firebase/firebase-android-sdk/issues/6941)
- Skip

### [Remote Config version 23.0.0](https://firebase.google.com/support/release-notes/android#remote-config_v23-0-0)
> - Improved how the SDK handles real-time requests when a Firebase project has exceeded its available quota for real-time services. Released in anticipation of future quota enforcement, this change is designed to fetch the latest template even when the quota is exhausted.

> [!BREAKING CHANGE]
> - **Breaking Change**: Updated `minSdkVersion` to API level 23 or higher.

> - **Breaking Change**: Stopped releasing the deprecated Kotlin extensions (KTX) module and removed it from the Firebase Android BoM. Instead, use the KTX APIs from the main module. For details, see the [FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration).

### Analytics version 22.1.2 ([link](https://firebase.google.com/support/release-notes/android#analytics_v22-1-2))
- Skip

### Analytics version 22.2.0 ([link](https://firebase.google.com/support/release-notes/android#analytics_v22-2-0))
- Skip

### Analytics version 22.3.0 ([link](https://firebase.google.com/support/release-notes/android#analytics_v22-3-0))
- Skip

### Analytics version 22.4.0 ([link](https://firebase.google.com/support/release-notes/android#analytics_v22-4-0))
- Skip

### Analytics version 22.5.0 ([link](https://firebase.google.com/support/release-notes/android#analytics_v22-5-0))
> - Internal code cleanup and optimizations.
- Skip

### Analytics version 23.0.0 ([link](https://firebase.google.com/support/release-notes/android#analytics_v23-0-0))
> - **Breaking Change**: Stopped releasing the deprecated Kotlin extensions (KTX) module and removed it from the Firebase Android BoM. Instead, use the KTX APIs from the main module. For details, see the [FAQ about this initiative](https://firebase.google.com/docs/android/kotlin-migration).

- Ok. Already doesn't use it in projects. Skip

</details>

---

### Breaking changes

1. The Android 15 edge-to-edge enforcement has been opted out by setting the `getTheme().applyStyle(R.style.OptOutEdgeToEdgeEnforcement, false);` flag in all the Activities. [SettingsActivity](https://gitlab.com/jackes/calendar/blob/b14920f61e691ff78e86a010b9d8392395c4247a/app/src/main/java/com/itbenefit/android/calendar/ui/settings/SettingsActivity.java#L73-73).

2. The StrictMode alarms that the every intent to update Widget is violates unsafe intent policy.

3. Changed `minSdkVersion` from 21 to 23. The RemoteConfig requirement. See more: https://firebase.google.com/support/release-notes/android#remote-config_v23-0-0

### Tests
- See the test results in [[Calendar 1.37] UPD: SDK 35, libs, tools](https://docs.google.com/spreadsheets/d/1YTVEYPuGEKf_liJt8nCxQL35ZRNfVYu0Hwb8Pr9FK0k/edit?gid=0#gid=0).
```

**Related issues (closes on merge, best effort):**
- #74 Bump target API level to 35, update libs and tools — https://gitlab.com/jackes/calendar/-/issues/74

### Commits (detailed)

#### 1. `ce12eeaa` Update dependencies and bump `minSdkVersion`

- SHA: `ce12eeaaa075778e368a9c743fe12a6776c1f929`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/ce12eeaaa075778e368a9c743fe12a6776c1f929
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-08-02T19:25:42.000+07:00

**Full commit message:**

```text
Update dependencies and bump `minSdkVersion`

Updated the following dependencies:
- `core-ktx` to 1.16.0
- `kotlin-stdlib-jdk7` to `kotlin-stdlib`
- `appcompat` to 1.7.1
- Firebase Bill of Materials (BoM) to 34.0.0 for `firebase-analytics` and `firebase-config`
- `play-services-analytics` to 18.1.1
- `mockito-inline` to `mockito-core` version 5.18.0
- `robolectric` to 4.15.1

Changed `minSdkVersion` from 21 to 23. The RemoteConfig requirement. See more: https://firebase.google.com/support/release-notes/android#remote-config_v23-0-0

Tests Android 15:
- Run unit-tests.
- Build and run am-release and am-debug versions.
```

**Diff (per commit):**

##### `app/build.gradle`

```diff
--- a/app/build.gradle
+++ b/app/build.gradle
@@ -8,7 +8,7 @@ android {
 
     defaultConfig {
         applicationId "com.itbenefit.android.calendar"
-        minSdkVersion 21
+        minSdkVersion 23
         targetSdkVersion 35
         compileSdk = 35
         buildToolsVersion = "35.0.0"
@@ -49,15 +49,18 @@ android {
 dependencies {
     implementation project(':lib')
 
-    implementation "androidx.core:core-ktx:1.13.1"
-    implementation "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version"
+    implementation "androidx.core:core-ktx:1.16.0"
+    implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
 
-    implementation "androidx.appcompat:appcompat:1.7.0"
+    implementation "androidx.appcompat:appcompat:1.7.1"
 
-    implementation 'com.google.firebase:firebase-analytics:22.1.0'
-    implementation 'com.google.firebase:firebase-config:22.0.0'
+    implementation platform('com.google.firebase:firebase-bom:34.0.0')
+    implementation 'com.google.firebase:firebase-analytics'
+    implementation 'com.google.firebase:firebase-config'
 
-    implementation 'com.google.android.gms:play-services-analytics:18.1.0' //TODO: what is is?
+    //TODO (shch): Deprecated, use the firebase-analytics instead
+    //  See more: https://developers.google.com/android/guides/setup?utm_source=chatgpt.com#list-dependencies
+    implementation 'com.google.android.gms:play-services-analytics:18.1.1'
     implementation 'net.xpece.android:support-preference:3.0.0'
     implementation ('com.vdurmont:emoji-java:5.1.1', {
         exclude group:'org.json', module:'json'
@@ -69,8 +72,8 @@ dependencies {
     implementation files ("libs/html-textview-4.0.aar")
 
     testImplementation 'junit:junit:4.13.2'
-    testImplementation 'org.mockito:mockito-inline:5.2.0'
-    testImplementation 'org.robolectric:robolectric:4.13'
+    testImplementation 'org.mockito:mockito-core:5.18.0'
+    testImplementation 'org.robolectric:robolectric:4.15.1'
 
     implementation project(":android-utils:library")
 }
```

##### `build.gradle`

```diff
--- a/build.gradle
+++ b/build.gradle
@@ -7,7 +7,7 @@ buildscript {
     }
     dependencies {
         classpath 'com.android.tools.build:gradle:8.12.0'
-        classpath 'com.google.gms:google-services:4.4.2'
+        classpath 'com.google.gms:google-services:4.4.3'
         classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
 
         // NOTE: Do not place your application dependencies here; they belong
```

#### 2. `d184f77c` Bump Android target SDK version

- SHA: `d184f77ccefe856e060513ec89b2a7dc08fe6fbd`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/d184f77ccefe856e060513ec89b2a7dc08fe6fbd
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-08-02T19:25:40.000+07:00

**Full commit message:**

```text
Bump Android target SDK version

Disabled the enforced edge-to-edge mode. Read more: https://developer.android.com/about/versions/15/behavior-changes-15#edge-to-edge

Tests Android 15:
- Open:
    - SettingsActivity.
    - LicenseInfoActivity.
    - WelcomeActivity.
    - TutorialActivity.
    - FAQActivity.
- Make sure all that activities doesn't intersect with the system bars and have its own status bar and nav bar.
```

**Diff (per commit):**

##### `.gitlab-ci.yml`

```diff
--- a/.gitlab-ci.yml
+++ b/.gitlab-ci.yml
@@ -6,18 +6,18 @@ variables:
 
   # ANDROID_COMPILE_SDK is the version of Android you're compiling with.
   # It should match compileSdkVersion.
-  ANDROID_COMPILE_SDK: "34"
+  ANDROID_COMPILE_SDK: "35"
 
   # ANDROID_BUILD_TOOLS is the version of the Android build tools you are using.
   # It should match buildToolsVersion.
-  ANDROID_BUILD_TOOLS: "34.0.0"
+  ANDROID_BUILD_TOOLS: "35.0.0"
 
   # It's what version of the command line tools we're going to download from the official site.
   # Official Site-> https://developer.android.com/studio/index.html
   # There, look down below at the cli tools only, sdk tools package is of format:
   #        commandlinetools-os_type-ANDROID_SDK_TOOLS_latest.zip
   # when the script was last modified for latest compileSdkVersion, it was which is written down below
-  ANDROID_SDK_TOOLS: "11076708"
+  ANDROID_SDK_TOOLS: "13114758"
 
 # Packages installation before running script
 before_script:
```

##### `app/build.gradle`

```diff
--- a/app/build.gradle
+++ b/app/build.gradle
@@ -9,9 +9,9 @@ android {
     defaultConfig {
         applicationId "com.itbenefit.android.calendar"
         minSdkVersion 21
-        targetSdkVersion 34
-        compileSdk 34
-        buildToolsVersion = "34.0.0"
+        targetSdkVersion 35
+        compileSdk = 35
+        buildToolsVersion = "35.0.0"
         versionCode 55
         versionName "1.37"
         resConfigs "ru"
```

##### `app/src/main/java/com/itbenefit/android/calendar/ui/FAQActivity.java`

```diff
--- a/app/src/main/java/com/itbenefit/android/calendar/ui/FAQActivity.java
+++ b/app/src/main/java/com/itbenefit/android/calendar/ui/FAQActivity.java
@@ -27,6 +27,9 @@ public class FAQActivity extends AppCompatActivity {
     protected void onCreate(Bundle savedInstanceState) {
         super.onCreate(savedInstanceState);
         requestWindowFeature(Window.FEATURE_NO_TITLE);
+
+        // TODO (shch): 25.07.2025 Remove once activity handle insets
+        getTheme().applyStyle(R.style.OptOutEdgeToEdgeEnforcement, false);
         setContentView(R.layout.activity_faq);
 
         int contentResId = getIntent().getIntExtra(EXTRA_CONTENT_RES_ID, 0);
```

##### `app/src/main/java/com/itbenefit/android/calendar/ui/LicenseInfoActivity.java`

```diff
--- a/app/src/main/java/com/itbenefit/android/calendar/ui/LicenseInfoActivity.java
+++ b/app/src/main/java/com/itbenefit/android/calendar/ui/LicenseInfoActivity.java
@@ -38,6 +38,8 @@ public class LicenseInfoActivity extends BillingActivity {
     public void onCreate(@Nullable Bundle savedInstanceState) {
         super.onCreate(savedInstanceState);
 
+        // TODO (shch): 25.07.2025 Remove once activity handle insets
+        getTheme().applyStyle(R.style.OptOutEdgeToEdgeEnforcement, false);
         setContentView(getLayoutResId());
 
         mTitleTextView = findViewById(R.id.titleTextView);
```

##### `app/src/main/java/com/itbenefit/android/calendar/ui/TutorialActivity.java`

```diff
--- a/app/src/main/java/com/itbenefit/android/calendar/ui/TutorialActivity.java
+++ b/app/src/main/java/com/itbenefit/android/calendar/ui/TutorialActivity.java
@@ -29,6 +29,8 @@ public class TutorialActivity extends AppCompatActivity {
 
         requestWindowFeature(Window.FEATURE_NO_TITLE);
 
+        // TODO (shch): 25.07.2025 Remove once activity handle insets
+        getTheme().applyStyle(R.style.OptOutEdgeToEdgeEnforcement, false);
         setContentView(R.layout.activity_tutorial);
 
         mViewPager = findViewById(R.id.viewPager);
```

##### `app/src/main/java/com/itbenefit/android/calendar/ui/WelcomeActivity.java`

```diff
--- a/app/src/main/java/com/itbenefit/android/calendar/ui/WelcomeActivity.java
+++ b/app/src/main/java/com/itbenefit/android/calendar/ui/WelcomeActivity.java
@@ -40,6 +40,8 @@ public class WelcomeActivity extends AppCompatActivity implements AlertDialogFra
         super.onCreate(savedInstanceState);
         requestWindowFeature(Window.FEATURE_NO_TITLE);
 
+        // TODO (shch): 25.07.2025 Remove once activity handle insets
+        getTheme().applyStyle(R.style.OptOutEdgeToEdgeEnforcement, false);
         setContentView(R.layout.activity_welcome);
 
         mInstructionsPlayer = findViewById(R.id.videoPlayer);
```

##### `app/src/main/java/com/itbenefit/android/calendar/ui/settings/SettingsActivity.java`

```diff
--- a/app/src/main/java/com/itbenefit/android/calendar/ui/settings/SettingsActivity.java
+++ b/app/src/main/java/com/itbenefit/android/calendar/ui/settings/SettingsActivity.java
@@ -69,6 +69,9 @@ public class SettingsActivity extends AppCompatActivity implements NoCalendarPer
     protected void onCreate(Bundle savedInstanceState) {
         super.onCreate(savedInstanceState);
 
+        // TODO (shch): 25.07.2025 Remove once activity handle insets
+        getTheme().applyStyle(R.style.OptOutEdgeToEdgeEnforcement, false);
+
         assert getSupportActionBar() != null;
         getSupportActionBar().setHomeButtonEnabled(true);
         getSupportActionBar().setDisplayHomeAsUpEnabled(true);
```

##### `app/src/main/res/values-v35/styles.xml`

```diff
--- /dev/null
+++ b/app/src/main/res/values-v35/styles.xml
@@ -0,0 +1,7 @@
+<?xml version="1.0" encoding="utf-8"?>
+<resources>
+    <!-- TODO: Remove once activities handle insets. -->
+    <style name="OptOutEdgeToEdgeEnforcement">
+        <item name="android:windowOptOutEdgeToEdgeEnforcement">true</item>
+    </style>
+</resources>
\ No newline at end of file
```

##### `app/src/main/res/values/styles.xml`

```diff
--- a/app/src/main/res/values/styles.xml
+++ b/app/src/main/res/values/styles.xml
@@ -98,4 +98,11 @@
         <item name="android:layout_height">match_parent</item>
     </style>
 
+    <!-- TODO: Remove once activities handle insets. -->
+    <style name="OptOutEdgeToEdgeEnforcement">
+        <!-- android:windowOptOutEdgeToEdgeEnforcement
+             isn't supported before SDK 35. This empty
+             style enables programmatically opting-out. -->
+    </style>
+
 </resources>
```

##### `key/build.gradle`

```diff
--- a/key/build.gradle
+++ b/key/build.gradle
@@ -6,9 +6,9 @@ android {
     defaultConfig {
         applicationId "com.itbenefit.android.calendar.key"
         minSdkVersion 8
-        targetSdkVersion 34
-        compileSdk 34
-        buildToolsVersion = '34.0.0'
+        targetSdkVersion 35
+        compileSdk = 35
+        buildToolsVersion = '35.0.0'
         versionCode 4
         versionName "1.3"
         setProperty("archivesBaseName", "calendar_key-$versionName")
```

#### 3. `8eaeae82` Bump Kotlin and Gradle versions

- SHA: `8eaeae829bf2cad7209b0fa4428694014eaabb5a`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/8eaeae829bf2cad7209b0fa4428694014eaabb5a
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-08-02T14:27:53.000+07:00

**Full commit message:**

```text
Bump Kotlin and Gradle versions

Tests Android 16:
- Build and run.
- Make sure the app launches.
```

**Diff (per commit):**

##### `build.gradle`

```diff
--- a/build.gradle
+++ b/build.gradle
@@ -1,12 +1,12 @@
 // Top-level build file where you can add configuration options common to all sub-projects/modules.
 buildscript {
-    ext.kotlin_version = '2.0.20'
+    ext.kotlin_version = '2.2.0'
     repositories {
         google()
         mavenCentral()
     }
     dependencies {
-        classpath 'com.android.tools.build:gradle:8.6.0'
+        classpath 'com.android.tools.build:gradle:8.12.0'
         classpath 'com.google.gms:google-services:4.4.2'
         classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
```

##### `gradle/wrapper/gradle-wrapper.properties`

```diff
--- a/gradle/wrapper/gradle-wrapper.properties
+++ b/gradle/wrapper/gradle-wrapper.properties
@@ -2,4 +2,4 @@ distributionBase=GRADLE_USER_HOME
 distributionPath=wrapper/dists
 zipStoreBase=GRADLE_USER_HOME
 zipStorePath=wrapper/dists
-distributionUrl=https\://services.gradle.org/distributions/gradle-8.7-bin.zip
\ No newline at end of file
+distributionUrl=https\://services.gradle.org/distributions/gradle-8.14.3-bin.zip
\ No newline at end of file
```

**Files touched in this MR (derived from commit diffs):**
- `.gitlab-ci.yml`
- `app/build.gradle`
- `app/src/main/java/com/itbenefit/android/calendar/ui/FAQActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/LicenseInfoActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/TutorialActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/WelcomeActivity.java`
- `app/src/main/java/com/itbenefit/android/calendar/ui/settings/SettingsActivity.java`
- `app/src/main/res/values-v35/styles.xml`
- `app/src/main/res/values/styles.xml`
- `build.gradle`
- `gradle/wrapper/gradle-wrapper.properties`
- `key/build.gradle`

---

## Merge request !59 Resolve #78 "[billing] Upgrade Google Play Billing Library"

- MR URL: https://gitlab.com/jackes/calendar/-/merge_requests/59
- State: merged
- Merged at: 2025-10-09T05:55:29.899Z
- Author: Maxim Shcherbakov
- Branches: `78-upgrade-google-play-billing-library` → `master`

**Description:**

```text
### Draft

### Linked
- [Android Utils !28](https://gitlab.com/jackes/android-utils/-/merge_requests/28) _"Resolve Calendar#78 [billing] Upgrade Google Play Billing Library"_

Closes #78
```

**Related issues (closes on merge, best effort):**
- #78 [billing] Upgrade Google Play Billing Library — https://gitlab.com/jackes/calendar/-/issues/78

### Commits (detailed)

#### 1. `d32fa039` [billing] Simplify `PlaySkuInfo` creation and testing

- SHA: `d32fa039d69b18dfb9dff2442f962a0ef2098f26`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/d32fa039d69b18dfb9dff2442f962a0ef2098f26
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-10-08T12:07:00.000+07:00

**Full commit message:**

```text
[billing] Simplify `PlaySkuInfo` creation and testing

This commit refactors the creation of `PlaySkuInfo` objects from `ProductDetails` and improves the associated tests.

Also added the `BillingTestUtils` helper that allows to call package-private constructor of the `ProductDetails` for testing.

Key changes:
- A new `PlaySkuInfo.parseFrom(productDetails)` factory method is returned, centralizing the mapping logic.
- `ProductDetailsMapper` is updated to expose a single `getPlaySkuInfo` method for a single `ProductDetails` object, simplifying its responsibility.
- `PlaySkuInfoRequest` now uses `PlaySkuInfo.parseFrom()` directly, removing the intermediate mapping step. It also adds logging for unfetched products.
- `ProductDetailsMapperTest` has been removed and its test cases have been migrated to a new, more focused `PlaySkuInfoTest`.
- Tests are updated to use real JSON data to construct `ProductDetails` objects via a new `BillingTestUtils.createProductDetails()` helper, eliminating complex mocking and making tests more robust and realistic.
```

**Diff (per commit):**

##### `android-utils`

```diff
--- a/android-utils
+++ b/android-utils
@@ -1 +1 @@
-Subproject commit 7ab622b8bf9804e70cd05ef4a98cdd4c2aab3b68
+Subproject commit 414f8e498b924569f0ba617a29833e0ac735dbda
```

#### 2. `0621d039` [billing] Upgrade Billing library to v8.0.0

- SHA: `0621d039e9e46ce27a54794c24523f121686ecc9`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/0621d039e9e46ce27a54794c24523f121686ecc9
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-09-30T19:04:23.000+07:00

**Full commit message:**

```text
[billing] Upgrade Billing library to v8.0.0

Update android-utils submodule

Key changes include:
- Replaced deprecated `SkuDetails` and related APIs with `ProductDetails`.
- Updated `BillingClient.newBuilder().enablePendingPurchases()` to accept `PendingPurchasesParams`.
- Adapted `PlayPurchaseFlow` to use `ProductDetailsParams` for launching the billing flow, including handling offer tokens for subscriptions.
- Updated `PlaySkuInfoRequest` to use `queryProductDetailsAsync`.
- Updated `PlayPurchasesRequest` to use `QueryPurchasesParams` for `queryPurchasesAsync`.
- Modified `PlaySkuId` to use `BillingClient.ProductType` constants.
- Updated `BillingClientMock` for testing to align with the new `ProductDetails` APIs.

Tests Android 13:
- Build and run.
- Open the license info screen.
- Make sure that the purchase info has been loaded.
- Tap the purchase button.
- Make sure that there are correct info in Billing purchase flow Activity.
```

**Diff (per commit):**

##### `android-utils`

```diff
--- a/android-utils
+++ b/android-utils
@@ -1 +1 @@
-Subproject commit d26295f0c9a8d513c8d41080da0c9c1a363c4357
+Subproject commit 7ab622b8bf9804e70cd05ef4a98cdd4c2aab3b68
```

**Files touched in this MR (derived from commit diffs):**
- `android-utils`

---

## Merge request !60 Resolve #77 "Error when no email client on the device"

- MR URL: https://gitlab.com/jackes/calendar/-/merge_requests/60
- State: merged
- Merged at: 2025-12-30T10:51:13.822Z
- Author: Maxim Shcherbakov
- Branches: `77-Error-when-no-email-client-on-the-device` → `master`

**Description:**

```text
Issue: You get a crash in the FeedbackDialog when attached debug info if there are no email client app on the device.

Fix: Catch the ActivityNotFoundException when trying to start the Activity with the email send Intent.

Tests Android 16:
- Remove/disable all email clients on the device.
- Run the app.
- Go to the settings.
- Tap the "Still have a question?"
- Check the "Attach debug info"
- Make sure the app doesn't crash and there Toast with the info has been displayed.

Closes #77
```

**Related issues (closes on merge, best effort):**
- #77 Error when no email client on the device — https://gitlab.com/jackes/calendar/-/issues/77

### Commits (detailed)

#### 1. `de400ebf` CI: Use eclipse-temurin as the base Docker image

- SHA: `de400ebfd7e05dab28d1800d26d49a71ed0340ff`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/de400ebfd7e05dab28d1800d26d49a71ed0340ff
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-12-25T21:47:17.000+07:00

**Full commit message:**

```text
CI: Use eclipse-temurin as the base Docker image

Issue: The openjdk images on Docker Hub are deprecated and many tags (including openjdk:17-jdk-slim) were recently removed.

Fix: Replace the openjdk with eclipse-temurin.
```

**Diff (per commit):**

##### `.gitlab-ci.yml`

```diff
--- a/.gitlab-ci.yml
+++ b/.gitlab-ci.yml
@@ -1,4 +1,4 @@
-image: openjdk:17-jdk-slim
+image: eclipse-temurin:17-jdk
 
 variables:
```

#### 2. `c76e52e8` Fix: FeedbackDialog crash when there are no email app

- SHA: `c76e52e8fb86c5b1c6ce5d2ce11c1f792f625e7c`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/c76e52e8fb86c5b1c6ce5d2ce11c1f792f625e7c
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-12-25T21:46:04.000+07:00

**Full commit message:**

```text
Fix: FeedbackDialog crash when there are no email app

Issue: You get a crash in the FeedbackDialog when attached debug info if there are no email client app on the device.

Fix: Catch the ActivityNotFoundException when trying to start the Activity with the email send Intent.

Tests Android 16:
- Remove/disable all email clients on the device.
- Run the app.
- Go to the settings.
- Tap the "Still have a question?"
- Check the "Attach debug info"
- Make sure the app doesn't crash and there Toast with the info has been displayed.
```

**Diff (per commit):**

##### `app/src/main/java/com/itbenefit/android/calendar/utils/SupportEmailHelper.kt`

```diff
--- a/app/src/main/java/com/itbenefit/android/calendar/utils/SupportEmailHelper.kt
+++ b/app/src/main/java/com/itbenefit/android/calendar/utils/SupportEmailHelper.kt
@@ -2,15 +2,21 @@
 
 package com.itbenefit.android.calendar.utils
 
+import android.content.ActivityNotFoundException
 import android.content.ClipData
 import android.content.Context
 import android.content.Intent
 import android.net.Uri
+import android.widget.Toast
 import com.itbenefit.android.calendar.R
 import java.io.File
 
 fun startSendEmailActivity(context: Context, subject: String, body: String, attachment: File?) {
-    context.startActivity(createSendEmailIntent(context, subject, body, attachment))
+    try {
+        context.startActivity(createSendEmailIntent(context, subject, body, attachment))
+    } catch (_: ActivityNotFoundException) {
+        Toast.makeText(context, R.string.email_client_not_found, Toast.LENGTH_LONG).show()
+    }
 }
 
 fun createSendEmailIntent(context: Context, subject: String, body: String, attachment: File?) =
```

##### `app/src/main/res/values-ru/strings.xml`

```diff
--- a/app/src/main/res/values-ru/strings.xml
+++ b/app/src/main/res/values-ru/strings.xml
@@ -210,6 +210,7 @@
     <string name="feedback_dialog_ok">Создать email</string>
     <string name="feedback_empty_message">Введите ваше сообщение</string>
     <string name="feedback_email_subject">Обратная связь</string>
+    <string name="email_client_not_found">Приложение для отправки email не найдено. Установите приложение для email и попробуйте снова.</string>
 
     <string name="perm_dialog_title">Отказанно в доступе</string>
     <string name="perm_dialog_message_calendar">Виджету требуется доступ к данным календаря. Иначе он не сможет отображать ваши календари и события.</string>
```

##### `app/src/main/res/values/strings.xml`

```diff
--- a/app/src/main/res/values/strings.xml
+++ b/app/src/main/res/values/strings.xml
@@ -211,6 +211,7 @@
     <string name="feedback_dialog_ok">Create email</string>
     <string name="feedback_empty_message">Please, type your message here</string>
     <string name="feedback_email_subject">Feedback</string>
+    <string name="email_client_not_found">No email app found. Please install an email app and try again.</string>
 
     <string name="perm_dialog_title">Permission denied</string>
     <string name="perm_dialog_message_calendar">Widget needs access to your calendar. Otherwise it could not show your calendars and events.</string>
```

**Files touched in this MR (derived from commit diffs):**
- `.gitlab-ci.yml`
- `app/src/main/java/com/itbenefit/android/calendar/utils/SupportEmailHelper.kt`
- `app/src/main/res/values-ru/strings.xml`
- `app/src/main/res/values/strings.xml`

---

## Merge request !61 Resolve #76 "Corners of the widget error layout are cropped in Android 12"

- MR URL: https://gitlab.com/jackes/calendar/-/merge_requests/61
- State: merged
- Merged at: 2025-12-30T11:06:44.796Z
- Author: Maxim Shcherbakov
- Branches: `76-Corners-of-the-widget-error-layout-are-cropped-in-Android-12` → `master`

**Description:**

```text
Tests Android 16:
- Run the app
- Go to the Debug Tools
- "Throw exception"
- Make sure the error layout corners are rounded.

Tests Android 10:
- Run the app
- Go to the Debug Tools
- "Throw exception"
- Make sure the error layout corners aren't rounded.

<details>
<summary>Screenshot</summary>

![Screenshot_20251227-190118](/uploads/193eb0077648caa42bd3bcafc1cf9d6e/Screenshot_20251227-190118.png){width=270 height=600}

</details>

Closes #76
```

**Related issues (closes on merge, best effort):**
- #76 Corners of the widget error layout are cropped in Android 12 — https://gitlab.com/jackes/calendar/-/issues/76

### Commits (detailed)

#### 1. `982b81df` Fix: widget error and loading layout corners cropped in Android 12+

- SHA: `982b81dfd8bbe2366ce769ceca65660712bcdc2c`
- Commit URL: https://gitlab.com/jackes/calendar/-/commit/982b81dfd8bbe2366ce769ceca65660712bcdc2c
- Author: Maxim Shcherbakov <maksimkachentr228@gmail.com>
- Created: 2025-12-30T17:56:19.000+07:00

**Full commit message:**

```text
Fix: widget error and loading layout corners cropped in Android 12+

Tests Android 16:
- Run the app
- Go to the Debug Tools
- "Throw exception"
- Make sure the error layout corners are rounded.

Tests Android 10:
- Run the app
- Go to the Debug Tools
- "Throw exception"
- Make sure the error layout corners aren't rounded.
```

**Diff (per commit):**

##### `app/src/main/res/drawable-v31/bg_def.xml`

```diff
--- /dev/null
+++ b/app/src/main/res/drawable-v31/bg_def.xml
@@ -0,0 +1,16 @@
+<?xml version="1.0" encoding="utf-8"?>
+<shape
+    xmlns:android="http://schemas.android.com/apk/res/android"
+    android:shape="rectangle">
+
+    <solid
+        android:color="#66000000" />
+
+    <stroke
+        android:color="#66565656"
+        android:width="1dp" />
+
+    <corners
+        android:radius="@android:dimen/system_app_widget_background_radius" />
+
+</shape>
```

**Files touched in this MR (derived from commit diffs):**
- `app/src/main/res/drawable-v31/bg_def.xml`

---
