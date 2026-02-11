#!/usr/bin/env python3
"""
التحقق النهائي الشامل من نظام الترجمة
Final Comprehensive Translation System Verification
"""

import sys

def verify_system():
    """التحقق الشامل من النظام | Comprehensive system verification"""
    
    print("=" * 70)
    print("🔍 التحقق النهائي من نظام الترجمة | Final Translation System Check")
    print("=" * 70)
    print()
    
    all_passed = True
    
    # 1. فحص الاستيراد
    print("1️⃣ فحص الاستيراد | Import Check:")
    try:
        from i18n import MESSAGES, SUPPORTED_LANGUAGES, t, get_guild_language, set_guild_language
        print("   ✅ جميع الوحدات تم استيرادها بنجاح")
        print("   ✅ All modules imported successfully")
    except Exception as e:
        print(f"   ❌ خطأ في الاستيراد | Import error: {e}")
        all_passed = False
        return False
    
    print()
    
    # 2. فحص عدد المفاتيح
    print("2️⃣ فحص عدد المفاتيح | Key Count Check:")
    key_count = len(MESSAGES)
    print(f"   📊 إجمالي المفاتيح | Total keys: {key_count}")
    
    if key_count >= 1590:
        print(f"   ✅ عدد ممتاز! (متوقع: 1598+)")
        print(f"   ✅ Excellent count! (Expected: 1598+)")
    elif key_count >= 1500:
        print(f"   ⚠️  جيد، لكن أقل من المتوقع")
        print(f"   ⚠️  Good, but less than expected")
    else:
        print(f"   ❌ عدد قليل جداً!")
        print(f"   ❌ Too few keys!")
        all_passed = False
    
    print()
    
    # 3. فحص اللغات المدعومة
    print("3️⃣ فحص اللغات | Languages Check:")
    print(f"   🌍 اللغات المدعومة | Supported: {SUPPORTED_LANGUAGES}")
    
    if 'ar' in SUPPORTED_LANGUAGES and 'en' in SUPPORTED_LANGUAGES:
        print("   ✅ العربية والإنجليزية مدعومتان")
        print("   ✅ Arabic and English are supported")
    else:
        print("   ❌ اللغات غير مكتملة!")
        print("   ❌ Languages incomplete!")
        all_passed = False
    
    print()
    
    # 4. فحص المفاتيح الأساسية
    print("4️⃣ فحص المفاتيح الأساسية | Essential Keys Check:")
    essential_keys = [
        "language.settings.title",
        "language.english",
        "language.arabic",
        "menu.settings.language_desc",
        "common.yes",
        "common.no",
        "action.save",
        "success.created",
        "error.not_found"
    ]
    
    missing = []
    for key in essential_keys:
        if key in MESSAGES:
            ar = MESSAGES[key].get('ar', 'N/A')
            en = MESSAGES[key].get('en', 'N/A')
            print(f"   ✅ {key}")
            print(f"      EN: {en[:40]}...")
            print(f"      AR: {ar[:40]}...")
        else:
            print(f"   ❌ {key} - مفقود!")
            missing.append(key)
            all_passed = False
    
    if missing:
        print(f"\n   ⚠️  مفاتيح مفقودة | Missing keys: {len(missing)}")
    
    print()
    
    # 5. فحص دالة الترجمة
    print("5️⃣ فحص دالة الترجمة | Translation Function Check:")
    
    try:
        # اختبار الإنجليزية
        result_en = t('common.yes', 'en')
        if result_en == 'Yes':
            print(f"   ✅ الإنجليزية: t('common.yes', 'en') = '{result_en}'")
        else:
            print(f"   ❌ الإنجليزية incorrect: '{result_en}' != 'Yes'")
            all_passed = False
        
        # اختبار العربية
        result_ar = t('common.yes', 'ar')
        if result_ar == 'نعم':
            print(f"   ✅ العربية: t('common.yes', 'ar') = '{result_ar}'")
        else:
            print(f"   ❌ العربية incorrect: '{result_ar}' != 'نعم'")
            all_passed = False
        
        # اختبار مع متغيرات
        result_var = t('time.seconds_ago', 'ar', count=30)
        print(f"   ✅ مع متغيرات: t('time.seconds_ago', 'ar', count=30) = '{result_var}'")
        
    except Exception as e:
        print(f"   ❌ خطأ في دالة الترجمة | Translation function error: {e}")
        all_passed = False
    
    print()
    
    # 6. فحص الترجمات الجديدة
    print("6️⃣ فحص الترجمات الجديدة | New Translations Check:")
    new_keys = [
        "common.loading",
        "status.online",
        "action.create",
        "nav.back",
        "success.saved",
        "error.permission",
        "confirm.delete",
        "calendar.january",
        "notif.new_message",
        "help.title"
    ]
    
    found_new = 0
    for key in new_keys:
        if key in MESSAGES:
            found_new += 1
    
    print(f"   📊 الترجمات الجديدة الموجودة: {found_new}/{len(new_keys)}")
    
    if found_new == len(new_keys):
        print("   ✅ جميع الترجمات الجديدة موجودة!")
        print("   ✅ All new translations present!")
    elif found_new >= len(new_keys) * 0.8:
        print("   ⚠️  معظم الترجمات موجودة")
    else:
        print("   ❌ الكثير من الترجمات الجديدة مفقودة!")
        all_passed = False
    
    print()
    
    # 7. فحص التغطية
    print("7️⃣ فحص التغطية | Coverage Check:")
    total_keys = len(MESSAGES)
    keys_with_both = 0
    keys_missing_ar = 0
    keys_missing_en = 0
    
    for key, translations in MESSAGES.items():
        has_en = 'en' in translations and translations['en']
        has_ar = 'ar' in translations and translations['ar']
        
        if has_en and has_ar:
            keys_with_both += 1
        elif not has_ar:
            keys_missing_ar += 1
        elif not has_en:
            keys_missing_en += 1
    
    coverage = (keys_with_both / total_keys * 100) if total_keys > 0 else 0
    
    print(f"   📊 المفاتيح الكاملة: {keys_with_both}/{total_keys}")
    print(f"   📊 التغطية: {coverage:.1f}%")
    
    if coverage >= 99:
        print("   ✅ تغطية ممتازة!")
        print("   ✅ Excellent coverage!")
    else:
        print(f"   ⚠️  تغطية جيدة لكن يمكن تحسينها")
        if keys_missing_ar:
            print(f"   ⚠️  مفقود العربية: {keys_missing_ar}")
        if keys_missing_en:
            print(f"   ⚠️  مفقود الإنجليزية: {keys_missing_en}")
    
    print()
    
    # 8. النتيجة النهائية
    print("=" * 70)
    print("📊 النتيجة النهائية | Final Result")
    print("=" * 70)
    
    if all_passed:
        print("🎉 ✅ نجح جميع الاختبارات!")
        print("🎉 ✅ All tests passed!")
        print()
        print("📝 تفاصيل النظام | System Details:")
        print(f"   • إجمالي المفاتيح: {key_count}")
        print(f"   • اللغات: {len(SUPPORTED_LANGUAGES)} (ar, en)")
        print(f"   • التغطية: {coverage:.1f}%")
        print()
        print("🚀 النظام جاهز للاستخدام!")
        print("🚀 System ready to use!")
        print()
        print("📖 كيفية الاستخدام | How to use:")
        print("   1. في Discord، اكتب: /settings")
        print("   2. اضغط على زر: 🌍 Language Settings")
        print("   3. اختر: العربية")
        print()
        return True
    else:
        print("❌ بعض الاختبارات فشلت!")
        print("❌ Some tests failed!")
        print()
        print("🔧 يرجى مراجعة الأخطاء أعلاه")
        print("🔧 Please review the errors above")
        print()
        return False


if __name__ == "__main__":
    try:
        success = verify_system()
        print("=" * 70)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ خطأ خطير | Critical error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
